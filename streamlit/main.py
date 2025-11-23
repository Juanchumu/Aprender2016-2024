import streamlit as st
import joblib
import pandas as pd


# Install streamlit if not already installed
#try:
#    import streamlit as st
#    import joblib
#    import pandas as pd

#except ImportError:
#    !pip install streamlit
#    !pip install joblib
#    !pip install pandas
#    import streamlit as st
#    import joblib
#    import pandas as pd

# Cargar el modelo

# Para utilizar localmente:
#model_matematica = joblib.load("/home/juan/virtual-env/UNLu/AA/2/Aprender2016-2024/streamlit/modelo_matematica.pkl")
#model_lengua = joblib.load("/home/juan/virtual-env/UNLu/AA/2/Aprender2016-2024/streamlit/modelo_lengua.pkl")

#Para utilizar en streamlit
model_matematica = joblib.load("/mount/src/aprender2016-2024/streamlit/modelo_matematica.pkl")
model_lengua = joblib.load("/mount/src/aprender2016-2024/streamlit/modelo_lengua.pkl")

# Título general
st.title("Aprender 2016-2024")
st.markdown("Esta aplicación permite estimar el valor de rendimiento academico en base a encuesta sobre su vida")
st.markdown("Alumnos:")
st.markdown(" Patrick Murayari - Bruno Weiss - Juan Jara")


# Tabs
tab1, tab2, tab3 = st.tabs([
    "1️⃣ Carga de Datos",
    "2️⃣ Revisión de Datos",
    "3️⃣ Predicción"
    ])

# ===================== TAB 1 =====================
with tab1:
    st.header("Carga de Datos de la encuesta Aprender")
    st.markdown("Complete los datos solicitados para realizar la predicción del valor de rendimiento")

    datos = {}

    st.subheader("¿En qué mes naciste?")
    datos['ap01_Agosto'] = st.number_input("Agosto", 1.0, 15793.0, 1.0)
    datos['ap01_Febrero'] = st.number_input("Febrero", 1.0, 15793.0, 1.0)
    datos['ap01_Mayo'] = st.number_input("Mayo", 1.0, 15793.0, 1.0)
    datos['ap01_Marzo'] = st.number_input("Marzo", 1.0, 15793.0, 1.0)
    datos['ap01_Septiembre'] = st.number_input("Septiembre", 1.0, 15793.0, 1.0)
    datos['ap01_Diciembre'] = st.number_input("Diciembre", 1.0, 15793.0, 1.0)
    datos['ap01_Abril'] = st.number_input("Abril", 1.0, 15793.0, 1.0)
    datos['ap01_Enero'] = st.number_input("Enero", 1.0, 15793.0, 1.0)
    datos['ap01_Julio'] = st.number_input("Julio", 1.0, 15793.0, 1.0)
    datos['ap01_Junio'] = st.number_input("Junio", 1.0, 15793.0, 1.0)
    datos['ap01_Multimarca'] = st.number_input("Multimarca (Mes de Nacimiento)", 1.0, 15793.0, 1.0)
    datos['ap01_Octubre'] = st.number_input("Octubre", 1.0, 15793.0, 1.0)
    datos['ap01_Noviembre'] = st.number_input("Noviembre", 1.0, 15793.0, 1.0)
    datos['ap01_No_disponible'] = st.number_input("No disponible (Mes de Nacimiento)", 1.0, 15793.0, 1.0)
    datos['ap01_Blanco'] = st.number_input("Blanco (Mes de Nacimiento)", 1.0, 15793.0, 1.0)

    st.subheader("¿En qué año naciste?")
    datos['ap02_2004'] = st.number_input("Año 2004", 1.0, 15793.0, 1.0)
    datos['ap02_Blanco'] = st.number_input("Blanco (Año de Nacimiento)", 1.0, 15793.0, 1.0)
    datos['ap02_2008'] = st.number_input("Año 2008", 1.0, 15793.0, 1.0)
    datos['ap02_2007'] = st.number_input("Año 2007", 1.0, 15793.0, 1.0)
    datos['ap02_2005'] = st.number_input("Año 2005", 1.0, 15793.0, 1.0)
    datos['ap02_2006'] = st.number_input("Año 2006", 1.0, 15793.0, 1.0)
    datos['ap02_Multimarca'] = st.number_input("Multimarca (Año de Nacimiento)", 1.0, 15793.0, 1.0)
    datos['ap02_2003'] = st.number_input("Año 2003", 1.0, 15793.0, 1.0)
    datos['ap02_No_disponible'] = st.number_input("No disponible (Año de Nacimiento)", 1.0, 15793.0, 1.0)

    st.subheader("¿Cuál es el sexo que figura en tu DNI?")
    datos['ap03_Femenino'] = st.number_input("Femenino", 1.0, 15793.0, 1.0)
    datos['ap03_Masculino'] = st.number_input("Masculino", 1.0, 15793.0, 1.0)
    datos['ap03_Multimarca'] = st.number_input("Multimarca (Sexo)", 1.0, 15793.0, 1.0)
    datos['ap03_No_disponible'] = st.number_input("No disponible (Sexo)", 1.0, 15793.0, 1.0)
    datos['ap03_Blanco'] = st.number_input("Blanco (Sexo)", 1.0, 15793.0, 1.0)

    st.subheader("¿En qué país naciste?")
    datos['ap04_Paraguay'] = st.number_input("País: Paraguay", 1.0, 15793.0, 1.0)
    datos['ap04_Perú'] = st.number_input("País: Perú", 1.0, 15793.0, 1.0)
    datos['ap04_Venezuela'] = st.number_input("País: Venezuela", 1.0, 15793.0, 1.0)
    datos['ap04_Bolivia'] = st.number_input("País: Bolivia", 1.0, 15793.0, 1.0)
    datos['ap04_En_un_país_de_Asia'] = st.number_input("País: En un país de Asia", 1.0, 15793.0, 1.0)
    datos['ap04_Colombia'] = st.number_input("País: Colombia", 1.0, 15793.0, 1.0)
    datos['ap04_Argentina'] = st.number_input("País: Argentina", 1.0, 15793.0, 1.0)
    datos['ap04_Chile'] = st.number_input("País: Chile", 1.0, 15793.0, 1.0)
    datos['ap04_En_un_país_de_Europa'] = st.number_input("País: En un país de Europa", 1.0, 15793.0, 1.0)
    datos['ap04_Uruguay'] = st.number_input("País: Uruguay", 1.0, 15793.0, 1.0)
    datos['ap04_Brasil'] = st.number_input("País: Brasil", 1.0, 15793.0, 1.0)
    datos['ap04_Otro_país_de_América'] = st.number_input("País: Otro país de América", 1.0, 15793.0, 1.0)
    datos['ap04_No_disponible'] = st.number_input("No disponible (País de Nacimiento)", 1.0, 15793.0, 1.0)
    datos['ap04_Blanco'] = st.number_input("Blanco (País de Nacimiento)", 1.0, 15793.0, 1.0)
    datos['ap04_Multimarca'] = st.number_input("Multimarca (País de Nacimiento)", 1.0, 15793.0, 1.0)

    st.subheader("¿Tu mamá papá o persona adulta responsable se reconoce de un pueblo índigena u originario o descendiente de una familia indígena u originaria?")
    datos['ap06_Sí'] = st.number_input("Sí (Origen Indígena)", 1.0, 15793.0, 1.0)
    datos['ap06_No'] = st.number_input("No (Origen Indígena)", 1.0, 15793.0, 1.0)
    datos['ap06_No_disponible'] = st.number_input("No disponible (Origen Indígena)", 1.0, 15793.0, 1.0)
    datos['ap06_Blanco'] = st.number_input("Blanco (Origen Indígena)", 1.0, 15793.0, 1.0)
    datos['ap06_Multimarca'] = st.number_input("Multimarca (Origen Indígena)", 1.0, 15793.0, 1.0)

    st.subheader("¿Tu mamá papá o persona adulta responsable se reconoce afrodescendiente o tiene antepasados negros o afrodescendientes?")
    datos['ap07_No_disponible'] = st.number_input("No disponible (Origen Afrodescendiente)", 1.0, 15793.0, 1.0)
    datos['ap07_Blanco'] = st.number_input("Blanco (Origen Afrodescendiente)", 1.0, 15793.0, 1.0)
    datos['ap07_Multimarca'] = st.number_input("Multimarca (Origen Afrodescendiente)", 1.0, 15793.0, 1.0)

    st.subheader("Queremos conocer más del lugar donde vivís. Por lo general dónde dormís más días?")
    datos['ap10_Blanco'] = st.number_input("Blanco (Lugar de Dormir)", 1.0, 15793.0, 1.0)
    datos['ap10_No_disponible'] = st.number_input("No disponible (Lugar de Dormir)", 1.0, 15793.0, 1.0)
    datos['ap10_Multimarca'] = st.number_input("Multimarca (Lugar de Dormir)", 1.0, 15793.0, 1.0)

    st.subheader("Aproximadamente cuántos libros hay en el lugar donde vivés? (pueden ser libros de poesía cuentos novelas manuales escolares diccionarios enciclopedias etc. en papel)")
    datos['ap19_No_hay_libros_en_formato_papel'] = st.number_input("No hay libros en papel", 1.0, 15793.0, 1.0)
    datos['ap19_Más_de_100_libros'] = st.number_input("Más de 100 libros", 1.0, 15793.0, 1.0)
    datos['ap19_De_51_a_100_libros'] = st.number_input("De 51 a 100 libros", 1.0, 15793.0, 1.0)
    datos['ap19_De_1_a_5_libros'] = st.number_input("De 1 a 5 libros", 1.0, 15793.0, 1.0)
    datos['ap19_No_disponible'] = st.number_input("No disponible (Libros)", 1.0, 15793.0, 1.0)
    datos['ap19_Blanco'] = st.number_input("Blanco (Libros)", 1.0, 15793.0, 1.0)
    datos['ap19_Multimarca'] = st.number_input("Multimarca (Libros)", 1.0, 15793.0, 1.0)


    st.subheader("Fuiste al jardín de infantes? ¿desde qué sala?")
    datos['ap24_Blanco'] = st.number_input("Blanco (Jardín de Infantes)", 1.0, 15793.0, 1.0)
    datos['ap24_No_disponible'] = st.number_input("No disponible (Jardín de Infantes)", 1.0, 15793.0, 1.0)


    st.subheader("¿Tenés materias previas?")
    datos['ap26_Multimarca'] = st.number_input("Multimarca (Materias previas)", 1.0, 15793.0, 1.0)
    datos['ap26_Blanco'] = st.number_input("Blanco (Materias previas)", 1.0, 15793.0, 1.0)
    datos['ap26_No_disponible'] = st.number_input("No disponible (Materias previas)", 1.0, 15793.0, 1.0)

    st.subheader("En lo que va del año cuántas faltas tenés?")
    datos['ap27_De_15_a_19_faltas'] = st.number_input("De 15 a 19 faltas", 1.0, 15793.0, 1.0)
    datos['ap27_De_5_a_14_faltas'] = st.number_input("De 5 a 14 faltas", 1.0, 15793.0, 1.0)
    datos['ap27_Menos_de_5_faltas'] = st.number_input("Menos de 5 faltas", 1.0, 15793.0, 1.0)
    datos['ap27_Ninguna_falta'] = st.number_input("Ninguna falta", 1.0, 15793.0, 1.0)
    datos['ap27_De_20_a_29_faltas'] = st.number_input("De 20 a 29 faltas", 1.0, 15793.0, 1.0)


    st.subheader("¿Cuáles fueron las tres razones principales por las que acumulaste faltas?")


    st.subheader("[Problemas de salud propios]")
    datos['ap28a_Selecciona'] = st.number_input("Problemas de salud propios (Selecciona)", 1.0, 15793.0, 1.0)
    datos['ap28a_Blanco'] = st.number_input("Problemas de salud propios (Blanco)", 1.0, 15793.0, 1.0)
    datos['ap28a_No_disponible'] = st.number_input("Problemas de salud propios (No disponible)", 1.0, 15793.0, 1.0)

    st.subheader("[Problemas de acceso a la escuela (debido al clima o al transporte)]")
    datos['ap28c_Selecciona'] = st.number_input("Problemas de acceso (Selecciona)", 1.0, 15793.0, 1.0)
    datos['ap28c_Blanco'] = st.number_input("Problemas de acceso (Blanco)", 1.0, 15793.0, 1.0)
    datos['ap28c_No_disponible'] = st.number_input("Problemas de acceso (No disponible)", 1.0, 15793.0, 1.0)

    st.subheader("[No tenía ganas de ir a la escuela]")
    datos['ap28d_Selecciona'] = st.number_input("No tenía ganas (Selecciona)", 1.0, 15793.0, 1.0)
    datos['ap28d_No_disponible'] = st.number_input("No tenía ganas (No disponible)", 1.0, 15793.0, 1.0)
    datos['ap28d_Blanco'] = st.number_input("No tenía ganas (Blanco)", 1.0, 15793.0, 1.0)

    st.subheader("[Estaba de vacaciones o de viaje]")
    datos['ap28j_Selecciona'] = st.number_input("Vacaciones o viaje (Selecciona)", 1.0, 15793.0, 1.0)
    datos['ap28j_No_disponible'] = st.number_input("Vacaciones o viaje (No disponible)", 1.0, 15793.0, 1.0)
    datos['ap28j_Blanco'] = st.number_input("Vacaciones o viaje (Blanco)", 1.0, 15793.0, 1.0)

    st.subheader("[Tenía que ayudar con las tareas del hogar]")
    datos['ap28e_Selecciona'] = st.number_input("Ayudar tareas hogar (Selecciona)", 1.0, 15793.0, 1.0)
    datos['ap28e_Blanco'] = st.number_input("Ayudar tareas hogar (Blanco)", 1.0, 15793.0, 1.0)
    datos['ap28e_No_disponible'] = st.number_input("Ayudar tareas hogar (No disponible)", 1.0, 15793.0, 1.0)



    st.subheader('Máximo nivel educativo padre')
    datos['Nivel_Ed_Padre_Terciario_universitario_posgrado_completo'] = st.number_input('Padre: Terciario universitario posgrado completo', 1.0, 15793.0, 1.0)
    datos['Nivel_Ed_Padre_Terciario_universitario_posgrado_incompleto'] = st.number_input('Padre: Terciario universitario posgrado incompleto', 1.0, 15793.0, 1.0)
    datos['Nivel_Ed_Padre_Secundaria_completo'] = st.number_input('Padre: Secundaria completo', 1.0, 15793.0, 1.0)
    datos['Nivel_Ed_Padre_Primaria_completo'] = st.number_input('Padre: Primaria completo', 1.0, 15793.0, 1.0)
    datos['Nivel_Ed_Padre_Multimarca'] = st.number_input('Padre: Multimarca (Nivel Educativo)', 1.0, 15793.0, 1.0)
    datos['Nivel_Ed_Padre_No_disponible'] = st.number_input('Padre: No disponible (Nivel Educativo)', 1.0, 15793.0, 1.0)
    datos['Nivel_Ed_Padre_Blanco'] = st.number_input('Padre: Blanco (Nivel Educativo)', 1.0, 15793.0, 1.0)

    st.subheader('Máximo nivel educativo madre')
    datos['Nivel_Ed_Madre_Terciario_universitario_posgrado_completo'] = st.number_input('Madre: Terciario universitario posgrado completo', 1.0, 15793.0, 1.0)
    datos['Nivel_Ed_Madre_Terciario_universitario_posgrado_incompleto'] = st.number_input('Madre: Terciario universitario posgrado incompleto', 1.0, 15793.0, 1.0)
    datos['Nivel_Ed_Madre_Secundaria_completo'] = st.number_input('Madre: Secundaria completo', 1.0, 15793.0, 1.0)
    datos['Nivel_Ed_Madre_Primaria_completo'] = st.number_input('Madre: Primaria completo', 1.0, 15793.0, 1.0)
    datos['Nivel_Ed_Madre_No_disponible'] = st.number_input('Madre: No disponible (Nivel Educativo)', 1.0, 15793.0, 1.0)
    datos['Nivel_Ed_Madre_Multimarca'] = st.number_input('Madre: Multimarca (Nivel Educativo)', 1.0, 15793.0, 1.0)
    datos['Nivel_Ed_Madre_Blanco'] = st.number_input('Madre: Blanco (Nivel Educativo)', 1.0, 15793.0, 1.0)

    st.subheader('Ubicacion')
    datos['lat'] = st.number_input('Latitud', -54.807306, -21.9470472, -34.577636)
    datos['lon'] = st.number_input('Longitud', -72.4188019, -54.0378533, -59.087643)

    st.subheader('Sobre-edad')
    datos['sobreedad_1_año_de_sobreedad_18_años_al_30_de_junio'] = st.number_input('1 año de sobreedad (18 años al 30 de junio)', 1.0, 15793.0, 1.0)
    datos['sobreedad_2_años_de_sobreedad_19_años_al_30_de_junio'] = st.number_input('2 años de sobreedad (19 años al 30 de junio)', 1.0, 15793.0, 1.0)

    st.subheader('Ambito de la escuela:   ')
    datos['ambito_binario'] = st.selectbox("Rural 0 | Urbano 1", [0, 1], index=1)


    st.subheader("Numero de Encuestados")
    datos['Nro_Encuestados'] = st.number_input('Nro:', 1.0, 15793.0, 1.0)






# ===================== TAB 2 =====================
with tab2:
    st.header("Datos cargados")
    st.markdown("Aquí puede revisar los datos ingresados antes de hacer la predicción.")
    st.json(datos)

# ===================== TAB 3 =====================
with tab3:
    st.header("Predicción del Rendimiento")
    st.markdown("Presione el botón para obtener una predicción basada en los datos ingresados.")

    input_df = pd.DataFrame([datos])

    # To ensure all columns are present and in correct order for the model
    # Get the feature names the model was trained on
    # Assuming the model objects (xgb_classifier, rf_classifier) have a 'feature_names_in_' attribute
    # If not, one would need to save X_train.columns during training and load it here.
    try:
        expected_features_matematica = model_matematica.feature_names_in_
        # Assuming both models use the same set of features. If not, this needs explicit handling.
        expected_features = expected_features_matematica

        # Create a dictionary with all expected features, initializing missing ones to 0.0
        input_data_processed = {feature: datos.get(feature, 0.0) for feature in expected_features}
        input_df = pd.DataFrame([input_data_processed])

    except AttributeError:
        st.warning("Could not retrieve feature names from the loaded model. Ensuring all inputs are present might be necessary for correct prediction.")
        # Fallback to the original less robust method if feature_names_in_ is not available
        input_df = pd.DataFrame([datos])
    prediccion_lengua = 0
    prediccion_matematica = 0
    if st.button("Predecir valor de rendimiento"):
        prediccion_matematica = model_matematica.predict(input_df)[0]
        prediccion_lengua = model_lengua.predict(input_df)[0]

        # Convertir predicciones a texto
    texto_mate = "Por debajo del nivel" 
    if (prediccion_matematica == 1):
        texto_mate = "Satisfactorio"
    texto_lengua = "Por debajo del nivel" 
    if (prediccion_lengua == 1):
        texto_lengua ="Satisfactorio"

    st.success(f"Predicción rendimiento matemática: {texto_mate}")
    st.success(f"Predicción rendimiento lengua: {texto_lengua}")

    st.caption("El modelo alcanza un accuracy del 81%.")
