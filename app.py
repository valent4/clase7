import streamlit as st
from textblob import TextBlob
from googletrans import Translator

# Configuración inicial
st.set_page_config(page_title="Análisis de Sentimientos", layout="centered")

# Estilo en blanco y negro con CSS
st.markdown("""
    <style>
        body {
            background-color: #ffffff;
            color: #000000;
        }
        .stApp {
            background-color: #ffffff;
            color: #000000;
        }
        .block-container {
            padding-top: 2rem;
        }
        .stTextArea textarea, .stTextInput input {
            background-color: #f7f7f7;
            color: #000000;
        }
        .stTextArea textarea:focus, .stTextInput input:focus {
            border: 1px solid #000000;
        }
        .stButton button {
            background-color: #000000;
            color: #ffffff;
        }
        .stButton button:hover {
            background-color: #333333;
        }
    </style>
""", unsafe_allow_html=True)

translator = Translator()

# Título
st.title("Análisis de Sentimientos")

# Subtítulo
st.markdown("Explora la polaridad y subjetividad de textos en un estilo monocromático y claro.")

# Información lateral
with st.sidebar:
    st.header("¿Qué significa cada cosa?")
    st.markdown("""
    **Polaridad**  
    Mide la orientación emocional del texto:  
    -1 = Negativo, 0 = Neutral, 1 = Positivo

    **Subjetividad**  
    Cuánto del texto es una opinión (1) o un hecho (0).
    """)

st.markdown("---")

# Distribución en columnas
col1, col2 = st.columns(2)

# Columna 1: Análisis de sentimiento
with col1:
    st.subheader("Análisis de sentimiento")
    text1 = st.text_area("Escribe un texto en español:")

    if text1:
        translation = translator.translate(text1, src="es", dest="en")
        translated_text = translation.text
        blob = TextBlob(translated_text)

        polarity = round(blob.sentiment.polarity, 2)
        subjectivity = round(blob.sentiment.subjectivity, 2)

        st.markdown("**Resultados:**")
        st.write("Polaridad:", polarity)
        st.write("Subjetividad:", subjectivity)

        if polarity >= 0.5:
            st.write("Sentimiento: Positivo")
        elif polarity <= -0.5:
            st.write("Sentimiento: Negativo")
        else:
            st.write("Sentimiento: Neutral")

# Columna 2: Corrección gramatical
with col2:
    st.subheader("Corrección en inglés")
    text2 = st.text_area("Texto en inglés para corregir:", key="correction")

    if text2:
        blob2 = TextBlob(text2)
        st.markdown("**Texto corregido:**")
        st.write(blob2.correct())

# Pie discreto
st.markdown("---")
st.caption("Aplicación en blanco y negro. Sin distracciones, solo análisis.")
