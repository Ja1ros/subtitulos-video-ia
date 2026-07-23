import os
import tempfile
import streamlit as st
from openai import OpenAI
from moviepy.editor import VideoFileClip
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="Subtitulos Automaticos para Videos", page_icon="🎥")
st.title("🎥 Generador Automatico de Subtitulos")
st.write("Sube un video y obten los subtitulos generados automaticamente en formato SRT.")

api_key = st.sidebar.text_input("OpenAI API Key", type="password")
uploaded_video = st.file_uploader("Sube un archivo de video", type=["mp4", "mov", "mkv", "avi"])


def format_timestamp(seconds: float) -> str:
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    secs = int(seconds % 60)
    millis = int((seconds - int(seconds)) * 1000)
    return f"{hours:02d}:{minutes:02d}:{secs:02d},{millis:03d}"


def build_srt(segments) -> str:
    lines = []
    for i, seg in enumerate(segments, start=1):
        start = format_timestamp(seg["start"])
        end = format_timestamp(seg["end"])
        lines.append(str(i))
        lines.append(f"{start} --> {end}")
        lines.append(seg["text"].strip())
        lines.append("")
    return "\n".join(lines)


if uploaded_video and api_key and st.button("Generar subtitulos"):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp4") as tmp_video:
        tmp_video.write(uploaded_video.read())
        video_path = tmp_video.name

    with st.spinner("Extrayendo audio del video..."):
        audio_path = video_path.replace(".mp4", ".mp3")
        clip = VideoFileClip(video_path)
        clip.audio.write_audiofile(audio_path)
        clip.close()

    client = OpenAI(api_key=api_key)
    with st.spinner("Transcribiendo audio con IA..."):
        with open(audio_path, "rb") as audio_file:
            transcript = client.audio.transcriptions.create(
                model="whisper-1",
                file=audio_file,
                response_format="verbose_json",
            )

    srt_content = build_srt(transcript.segments)
    st.success("Subtitulos generados correctamente.")
    st.text_area("Vista previa del archivo SRT", srt_content, height=300)
    st.download_button(
        "Descargar subtitulos (.srt)",
        data=srt_content,
        file_name="subtitulos.srt",
        mime="text/plain",
    )

    os.remove(video_path)
    os.remove(audio_path)
elif not api_key:
    st.info("Ingresa tu API Key de OpenAI en la barra lateral para comenzar.")
