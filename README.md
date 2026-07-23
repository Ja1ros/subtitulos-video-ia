# Generador Automatico de Subtitulos para Videos

Aplicacion que extrae el audio de un video, lo transcribe usando IA (Whisper de OpenAI) y genera un archivo de subtitulos en formato SRT.

## Caracteristicas

- Carga de archivos de video (mp4, mov, mkv, avi).
- Extraccion automatica del audio.
- Transcripcion con marcas de tiempo usando el modelo Whisper.
- Generacion y descarga de archivo .srt listo para usar.

## Stack tecnologico

- Python 3.10+
- Streamlit
- MoviePy
- OpenAI API (Whisper)

## Instalacion

```bash
git clone https://github.com/Ja1ros/subtitulos-video-ia.git
cd subtitulos-video-ia
pip install -r requirements.txt
```

Nota: MoviePy requiere que FFmpeg este instalado en el sistema.

## Uso

```bash
streamlit run app.py
```

1. Ingresa tu API Key de OpenAI en la barra lateral.
2. Sube un archivo de video.
3. Presiona "Generar subtitulos".
4. Descarga el archivo .srt generado.

## Variables de entorno

Crea un archivo `.env` basado en `.env.example` si prefieres no ingresar la API Key manualmente.

## Proximas mejoras

- Soporte para multiples idiomas de salida.
- Edicion manual de los subtitulos antes de exportar.
- Quemado de subtitulos directamente en el video.

## Licencia

Proyecto con fines educativos y de portafolio.
