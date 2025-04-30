import streamlit as st
from textblob import TextBlob
from googletrans import Translator

# Configuración básica
st.set_page_config(page_title="Análisis de Sentimientos", layout="centered")

translator = Translator()

# Título principal
st.title("Análisis de Sentimientos con TextBlob")

# Introducción breve
st.markdown("Analiza la polaridad y subjetividad de un texto de forma simple.")

# Información lateral
with st.sidebar:
    st.header("Información útil")
    st.markdown("""
    **Polaridad**  
    Indica si el sentimiento del texto es positivo, negativo o neutral.  
    Rango: -1 (muy negativo) a 1 (muy positivo).

    **Subjetividad**  
    Mide qué tan subjetivo (opiniones, emociones) u objetivo (hechos) es el texto.  
    Rango: 0 (objetivo) a 1 (subjetivo).
    """)

st.markdown("---")

# Crear las columnas
col1, col2 = st.columns(2)

# Columna 1: Análisis de Polaridad y Subjetividad
with col1:
    st.subheader("Análisis de Polaridad y Subjetividad")
    text1 = st.text_area("Escribe una frase en español:")

    if text1:
        translation = translator.translate(text1, src="es", dest="en")
        translated_text = translation.text
        blob = TextBlob(translated_text)

        polarity = round(blob.sentiment.polarity, 2)
        subjectivity = round(blob.sentiment.subjectivity, 2)

        st.markdown("**Resultados**")
        st.write("Polaridad:", polarity)
        st.write("Subjetividad:", subjectivity)

        if polarity >= 0.5:
            st.write("Sentimiento: Positivo")
        elif polarity <= -0.5:
            st.write("Sentimiento: Negativo")
        else:
            st.write("Sentimiento: Neutral")

# Columna 2: Corrector de texto en inglés
with col2:
    st.subheader("Corrección de texto en inglés")
    text2 = st.text_area("Escribe un texto en inglés para corregir:", key="correction")

    if text2:
        blob2 = TextBlob(text2)
        st.markdown("**Texto corregido:**")
        st.write(blob2.correct())

# Pie de página discreto
st.markdown("---")
st.caption("Aplicación desarrollada como demostración del uso de TextBlob y Google Translate.")

