# Análisis de Aspiraciones Futuras y Rendimiento Académico: El Rol del Apoyo Familiar en Estudiantes Secundarios (Aprender 2016-2024)

### Responsables:
* Patrick Murayari
* Bruno Weiss 
* Juan Jara. 

#### Fecha de inicio: 01/09/25

#### Organización: Universidad Nacional de Luján
### Materia: Aprendizaje Automatico


# Modelado:

Enlace a colab modelado:
* https://colab.research.google.com/drive/1qpRfe-2AKlWWSW1-I6y8tQEbHuTI8rLp?usp=sharing

### Enfoque adoptado y justificación:
El objetivo del proyecto fue construir modelos de clasificación capaces de predecir el nivel de desempeño del estudiante en dos áreas: Matemática y Lengua, utilizando dos categorías:

* Satisfactorio
* Por debajo del nivel satisfactorio

Para resolver este problema se adoptó un enfoque supervisado, ya que el dataset contaba con etiquetas previamente definidas. Se evaluaron múltiples algoritmos de clasificación (AdaBoost, Random Forest, XGBoost y MLP) con el propósito de comparar su rendimiento y seleccionar la mejor alternativa para cada área disciplinar.
La elección de estos modelos se justificó por sus características:

* AdaBoost: robusto ante ruido y útil para capturar patrones simples.
* Random Forest: muy estable en datos tabulares, con buena capacidad generalizadora.
* XGBoost: excelente rendimiento en problemas con interacciones complejas entre variables.
* MLP (Perceptrón Multicapa): permite capturar relaciones no lineales entre los atributos.

El uso de varios algoritmos permitió identificar qué arquitectura se adaptaba mejor a cada área.
Como resultado final, se seleccionaron dos modelos diferentes:

* MLP para Matemática.
* Random Forest para Lengua.

### Implementación del modelo o sistema de base

Los datos ya se encontraban codificados mediante One-Hot Encoding, debido a que las preguntas de la encuesta consideraban

* Respuestas en blanco: cuando el alumno no completaba nada de la seccion
* Multimarcas: cuando el alumno marcaba multiples invalidando la respuesta

pero tambien presentaban múltiples inconsistencias entre distintos años

* Variación en nombres de columnas: ap28 -> ap01_26
* Preguntas presentes solo algunos años
* Diferencias en disponibilidad de variables: habia preguntas faltantes

Esto obligó a descartar atributos inestables y conservar únicamente las columnas comunes y consistentes (renombradas o agrupando) a lo largo del tiempo.

### El pipeline de trabajo fue:

* Integración de datasets de distintos años y depuración de inconsistencias.
* Selección de variables consistentes y eliminación de columnas incompatibles.
* División del dataset en conjuntos de entrenamiento y prueba.
* Entrenamiento de los modelos ADA, RF, XGBoost y MLP.
* Comparación sistemática del rendimiento de cada modelo.
* Selección del mejor modelo para Matemática y para Lengua.

El entrenamiento se realizó utilizando Scikit-Learn 1.6.1, lo cual facilita la reproducibilidad del proceso y permite una integración sencilla con la interfaz desarrollada en Streamlit.

### Evaluación de la solución
Dado que se trata de un problema de clasificación binaria, la métrica principal utilizada fue accuracy, por dos motivos:
Las clases presentan un balance aceptable.
La institución requiere una predicción general correcta del nivel de desempeño.
Se utilizaron métricas complementarias (como F1 y la matriz de confusión) para verificar el comportamiento ante posibles desbalances y analizar errores específicos, pero la métrica reportada como principal fue accuracy.
Los resultados mostraron diferencias entre áreas:

* En Matemática, el MLP obtuvo el mejor rendimiento, capturando relaciones no lineales entre las variables.
* En Lengua, el Random Forest tuvo el desempeño más sólido y estable, superando a los demás modelos basados en boosting y redes neuronales.



# Streamlit

Enlace a streamlit:
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
