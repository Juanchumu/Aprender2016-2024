# Análisis de Aspiraciones Futuras y Rendimiento Académico: El Rol del Apoyo Familiar en Estudiantes Secundarios (Aprender 2016-2024)

### Responsables:
* Patrick Murayari
* Bruno Weiss 
* Juan Jara. 

#### Fecha de inicio: 01/09/25

#### Organización: Universidad Nacional de Luján
### Materia: Aprendisaje Automatico



enlace a colab modelado:
https://colab.research.google.com/drive/1qpRfe-2AKlWWSW1-I6y8tQEbHuTI8rLp?usp=sharing

# Streamlit

* enlace a streamlit:
* https://aprender2016-2024-aprendizaje-automatico-2025.streamlit.app/

### Simulación del uso del sistema
El prototipo en Streamlit permite ingresar nuevos datos y obtener una clasificación entre satisfactorio y por debajo del nivel satisfactorio. Esto replica cómo funcionaría en un entorno real: el usuario envía datos crudos y recibe una respuesta procesada por el modelo.

### Propuesta de despliegue en un entorno real

#### Arquitectura recomendada:

* Frontend: Streamlit (o una web más formal si se requiere).
* Backend: API en FastAPI o Flask, donde está cargado el modelo.
* Infraestructura: Contenedores Docker y despliegue en cloud (AWS, Azure, GCP, Render, Railway, etc.).

Flujo:
Usuario → Streamlit → API FastAPI → Modelo → Respuesta

#### Recursos necesarios
* Hardware:
	* Modelos clásicos: 1 CPU + 1–2 GB RAM.
	* Modelos más pesados: CPU/GPU según necesidad.

#### Software:
* Python 3.10+, Streamlit, FastAPI, Docker, GitHub/GitLab CI/CD.

### Alternativas para escalar
* Vertical: Aumentar RAM/CPU/GPU del servidor.
* Horizontal: Múltiples réplicas del backend con un balanceador de carga.
* Serverless: AWS Lambda / Cloud Run para autoescalado según demanda.
* APIs externas: Usar servicios como OpenAI/HuggingFace si el modelo es muy pesado.
* MLOps: Trackeo de versiones, monitoreo de drift y automatización del ciclo de vida del modelo.
