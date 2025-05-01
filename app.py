import streamlit as st
from textblob import TextBlob
from googletrans import Translator
from streamlit_lottie import st_lottie
import json

# Traductor
translator = Translator()

# Estilo visual oscuro y coherente con la animación
st.markdown("""
    <style>
    .stApp {
        background-color: #0e1117;
        color: #fafafa;
    }
    .block-container {
        padding: 2rem;
    }
    </style>
""", unsafe_allow_html=True)

# Animación Lottie
with open('Animation17.json') as source:
    animation = json.load(source)
st.lottie(animation, width=350)

# Título con concepto emocional
st.title("🎤 Dale voz a tus emociones")
st.markdown("Descubre el tono emocional de tus palabras y cómo suenan al mundo.")

# Selector de estilo de voz (opcional)
voz = st.selectbox("Elige tu estilo de voz:", ["🎙️ Neutra", "🔥 Apasionada", "🧠 Reflexiva", "📊 Analítica"])

# Sidebar con explicación
with st.sidebar:
    st.subheader("📈 Polaridad y Subjetividad")
    st.markdown("""
    - **Polaridad**: ¿Tu texto expresa alegría, tristeza o neutralidad? (Rango de -1 a 1)
    - **Subjetividad**: ¿Es una opinión o un hecho? (Rango de 0 a 1)
    """)

# Análisis de texto
with st.expander('🔍 Analiza tus palabras'):
    text1 = st.text_area('Escribe una frase o texto para analizar:')

    if text1:
        # Traducir a inglés para mejor análisis con TextBlob
        translation = translator.translate(text1, src="es", dest="en")
        trans_text = translation.text
        blob = TextBlob(trans_text)

        polarity = round(blob.sentiment.polarity, 2)
        subjectivity = round(blob.sentiment.subjectivity, 2)

        # Mostrar resultados
        st.markdown(f"** Polaridad:** {polarity}")
        st.markdown(f"** Subjetividad:** {subjectivity}")

        # Interpretación según polaridad
        if polarity >= 0.5:
            st.success('Tu voz suena optimista y alegre 😊')
        elif polarity <= -0.5:
            st.error('Tu voz refleja tristeza o molestia 😔')
        else:
            st.info('Tu voz transmite calma o neutralidad 😐')

# Corrección gramatical
with st.expander(' Corrección en inglés'):
    text2 = st.text_area('Escribe una frase en inglés para corregir:', key='correccion')

    if text2:
        blob2 = TextBlob(text2)
        corrected = blob2.correct()
        st.markdown(f"**Versión corregida:** {corrected}")

