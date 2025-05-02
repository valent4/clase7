import streamlit as st
from textblob import TextBlob
from googletrans import Translator

st.set_page_config(page_title="Análisis de Sentimientos", layout="centered")

# CSS mejorado y forzado
st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=Nunito:wght@400;600;700&display=swap" rel="stylesheet">
<style>
    html, body, [class*="css"]  {
        background-color: #F5F7FB !important;
        font-family: 'Nunito', sans-serif !important;
        color: #383031;
    }
    [data-testid="stTextInput"] input, [data-testid="stTextArea"] textarea {
        background-color: #E6ECFC !important;
        color: #383031 !important;
        border-radius: 12px !important;
        padding: 15px !important;
        font-size: 16px !important;
        border: none !important;
        box-shadow: 0px 4px 12px rgba(0,0,0,0.05);
    }
    [data-testid="stButton"] button {
        background-color: #A9B7F5 !important;
        color: white !important;
        border-radius: 12px !important;
        padding: 12px 24px !important;
        font-size: 16px !important;
        font-weight: 600;
        transition: all 0.3s ease-in-out;
        box-shadow: 0px 4px 10px rgba(0,0,0,0.08);
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
        background-color: #CDEDD2 !important;
        border-radius: 12px !important;
        color: #3F734C !important;
    }
    .stError {
        background-color: #FAD4D7 !important;
        border-radius: 12px !important;
        color: #A74449 !important;
    }
    .stInfo {
        background-color: #D6E8FB !important;
        border-radius: 12px !important;
        color: #426785 !important;
    }
    footer, header {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

translator = Translator()

st.markdown("<h1 style='text-align: center;'>🧠 Análisis de Sentimientos</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Analiza la polaridad y subjetividad de un texto y recibe una reacción emocional.</p>", unsafe_allow_html=True)
st.markdown("---")

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

col1, col2 = st.columns(2)

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

with col2:
    st.subheader("✏️ Corrector de texto en inglés")
    text2 = st.text_area("Escribe un texto en inglés para corregir:", key="correction")

    if text2:
        blob2 = TextBlob(text2)
        st.markdown("**Texto corregido:**")
        st.write(blob2.correct())

st.markdown("---")
st.caption("💻 Desarrollado por Valentina • Powered by TextBlob & Google Translate")






