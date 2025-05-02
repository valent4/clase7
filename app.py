import streamlit as st
from textblob import TextBlob
from googletrans import Translator

# Configuración de página
st.set_page_config(page_title="Análisis de Sentimientos", layout="centered")

# Estilos pastel tipo app original
st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap" rel="stylesheet">
<style>
    html, body, [class*="css"]  {
        background-color: #F0E6FA !important;
        font-family: 'Poppins', sans-serif !important;
        color: #383031;
    }
    [data-testid="stTextInput"] input, [data-testid="stTextArea"] textarea {
        background-color: #E6ECFC !important;
        color: #383031 !important;
        border-radius: 12px !important;
        padding: 15px !important;
        font-size: 16px !important;
        border: none !important;
        box-shadow: 0px 4px 8px rgba(0,0,0,0.05);
    }
    [data-testid="stButton"] button {
        background-color: #A9B7F5 !important;
        color: white !important;
        border-radius: 12px !important;
        padding: 10px 22px !important;
        font-size: 16px !important;
        font-weight: 600;
        transition: all 0.3s ease-in-out;
        box-shadow: 0px 4px 10px rgba(0,0,0,0.06);
        border: none;
    }
    [data-testid="stButton"] button:hover {
        background-color: #8A9DEB !important;
        transform: scale(1.02);
    }
    h1, h2, h3 {
        color: #383031 !important;
    }
    .stSuccess {
        background-color: #D9F3E3 !important;
        border-radius: 12px !important;
        color: #355C47 !important;
    }
    .stError {
        background-color: #FBE6E8 !important;
        border-radius: 12px !important;
        color: #A74449 !important;
    }
    .stInfo {
        background-color: #DDEBFB !important;
        border-radius: 12px !important;
        color: #3E5F88 !important;
    }
    footer, header {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# Funcionalidad
translator = Translator()

st.markdown("<h1 style='text-align: center;'>🌸 Análisis de Sentimientos</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Explora la polaridad y subjetividad de tus textos con una reacción emocional.</p>", unsafe_allow_html=True)
st.markdown("---")

with st.sidebar:
    st.header("🧾 ¿Qué mide esta app?")
    st.markdown("""
    **Polaridad**  
    Valor entre -1 (negativo) y 1 (positivo).  

    **Subjetividad**  
    Valor entre 0 (objetivo) y 1 (subjetivo).

    ---
    ✨ Consejo: Escribe algo que te salga del corazón para ver la reacción.
    """)

col1, col2 = st.columns(2)

with col1:
    st.subheader("💬 Análisis emocional")
    text1 = st.text_area("Escribe una frase en español:")

    if text1:
        translation = translator.translate(text1, src="es", dest="en")
        translated_text = translation.text
        blob = TextBlob(translated_text)

        polarity = round(blob.sentiment.polarity, 2)
        subjectivity = round(blob.sentiment.subjectivity, 2)

        st.markdown("**Resultados:**")
        st.write("🔵 Polaridad:", polarity)
        st.write("🟡 Subjetividad:", subjectivity)

        st.markdown("**🌟 Reacción del sistema:**")
        if polarity >= 0.5:
            st.success("¡Eso fue muy positivo! Me hizo sonreír 💜")
        elif polarity <= -0.5:
            st.error("Eso suena un poco triste... estoy aquí contigo 💔")
        else:
            st.info("Tu texto es neutro. A veces está bien simplemente observar 🌀")

with col2:
    st.subheader("✍️ Corrector de inglés")
    text2 = st.text_area("Escribe un texto en inglés para corregir:", key="correction")

    if text2:
        blob2 = TextBlob(text2)
        st.markdown("**Texto corregido:**")
        st.write(blob2.correct())

st.markdown("---")
st.caption("🎀 Desarrollado por Valentina • Powered by TextBlob & Google Translate")






