import streamlit as st
from textblob import TextBlob
from googletrans import Translator

# Configuración de la página
st.set_page_config(page_title="Análisis de Sentimientos", layout="centered")

# Estilos personalizados
st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=Nunito:wght@400;600;700&display=swap" rel="stylesheet">
<style>
    html, body, .stApp {
        background-color: #F6F8FB;
        color: #383031;
        font-family: 'Nunito', sans-serif;
    }

    .stTextInput > div > div > input, textarea, .stTextArea textarea {
        background-color: #E3ECF9 !important;
        color: #383031 !important;
        border-radius: 16px;
        padding: 15px;
        font-size: 16px;
        box-shadow: 0px 2px 6px rgba(0,0,0,0.05);
    }

    .stButton > button {
        background-color: #A9B7F5;
        color: white;
        border-radius: 16px;
        font-size: 16px;
        padding: 12px 24px;
        font-weight: bold;
        transition: 0.2s ease-in-out;
        box-shadow: 0px 2px 6px rgba(0,0,0,0.1);
    }

    .stButton > button:hover {
        background-color: #90A3E8;
        transform: scale(1.03);
    }

    h1, h2, h3 {
        color: #383031;
    }

    .stSuccess {
        background-color: #BCE5C7;
        border: 1px solid #A1D8A3;
        color: #4F8A55;
        border-radius: 16px;
        padding: 10px;
    }

    .stError {
        background-color: #F9CEDF;
        border: 1px solid #F1A1A6;
        color: #D36B6F;
        border-radius: 16px;
        padding: 10px;
    }

    .stInfo {
        background-color: #D3E8FA;
        border: 1px solid #A3CDE7;
        color: #537C91;
        border-radius: 16px;
        padding: 10px;
    }

    .block-container {
        padding-top: 2rem;
    }

    .stMarkdown {
        color: #383031;
    }
</style>
""", unsafe_allow_html=True)

translator = Translator()

# Título y subtítulo
st.markdown("<h1 style='text-align: center;'>🧠 Análisis de Sentimientos</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Analiza la polaridad y subjetividad de un texto y recibe una reacción emocional.</p>", unsafe_allow_html=True)

st.markdown("---")

# Sidebar
with st.sidebar:
    st.header("ℹ️ ¿Qué mide esta app?")
    st.markdown("""
    **Polaridad**  
    Valor entre -1 (muy negativo) y 1 (muy positivo).  
    **Subjetividad**  
    Valor entre 0 (muy objetivo) y 1 (muy subjetivo).

    ---
    🧩 **Tip:** Escribe algo sincero para ver cómo reacciona la IA.
    """)

# Columnas principales
col1, col2 = st.columns(2)

# Columna 1: Análisis de sentimientos
with col1:
    st.subheader("🔍 Análisis emocional del texto")
    text1 = st.text_area("Escribe una frase en español:")

    if text1:
        translation = translator.translate(text1, src="es", dest="en")
        translated_text = translation.text
        blob = TextBlob(translated_text)

        polarity = round(blob.sentiment.polarity, 2)
        subjectivity = round(blob.sentiment.subjectivity, 2)

        st.markdown("**Resultados del análisis:**")
        st.write("🔵 Polaridad:", polarity)
        st.write("🟡 Subjetividad:", subjectivity)

        st.markdown("**🤖 Reacción del sistema:**")
        if polarity >= 0.5:
            st.success("¡Qué bonito lo que escribiste! Se siente muy positivo 🌟")
        elif polarity <= -0.5:
            st.error("Veo que hay sentimientos negativos... Si necesitas hablar, aquí estoy. 💙")
        else:
            st.info("Tu texto tiene un tono neutral. ¿Quieres contarme más? 🤔")

# Columna 2: Corrector en inglés
with col2:
    st.subheader("✏️ Corrector de texto en inglés")
    text2 = st.text_area("Escribe un texto en inglés para corregir:", key="correction")

    if text2:
        blob2 = TextBlob(text2)
        st.markdown("**Texto corregido:**")
        st.write(blob2.correct())

# Pie de página
st.markdown("---")
st.caption("💻 Desarrollado por Valentina • Powered by TextBlob & Google Translate")






