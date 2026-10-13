# Cuestionario de Medicina · Módulo 2

Proyecto Flask independiente. Contiene 100 preguntas sustentadas en las páginas presentes de los ocho PDF compartidos. No contiene los PDF. Cada examen mixto toma 20 preguntas aleatorias; por tema muestra tantas preguntas como haya en ese tema. Las opciones se barajan y puede activarse o desactivarse la corrección inmediata.

## Probarlo localmente

```bash
cd modulo2
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

Abre http://127.0.0.1:5000. En Windows activa el entorno con `.venv\\Scripts\\activate`.

## Publicar como página nueva

Sube **solo esta carpeta `modulo2`** como raíz de un repositorio propio de GitHub. En Render crea un nuevo *Web Service* vinculado a ese repositorio; selecciona entorno Python, comando de construcción `pip install -r requirements.txt` y comando de inicio `gunicorn app:app`. El archivo `render.yaml` permite alternativamente crear un Blueprint desde el repositorio. Cuando Render indique que el servicio está activo, abre la URL HTTPS pública que te entregue y compártela. Será un enlace nuevo, distinto al enlace de Módulo 1. La disponibilidad y condiciones del servicio de alojamiento dependen de tu cuenta y plan.

## Fuentes

Las referencias `page` indican la numeración impresa, no el número de hoja que muestra el lector PDF. En `HarperCap 28 S14.pdf` solo se citan las páginas 281–298 que aparecen en el archivo. `HARPER Cap19Glucosa.pdf` repite fragmentos de los capítulos 18–19 y se empleó solo como referencia cruzada; el banco evita duplicarlos. `Semana 11 Bioquímica Pág 156, 162.pdf` se usó para contrastar glucogenólisis y enfermedad de Von Gierke.
