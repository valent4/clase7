import streamlit as st
from textblob import TextBlob
from googletrans import Translator

# Configuración de página
st.set_page_config(page_title="Análisis de Sentimientos", layout="centered")

# Estilo personalizado completo con tonos pastel claros
st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap" rel="stylesheet">
<style>
    html, body, [class*="css"]  {
        background-color: #F8F4FF !important;
        font-family: 'Poppins', sans-serif !important;
        color: #383031;
    }

    [data-testid="stTextInput"] input, 
    [data-testid="stTextArea"] textarea {
        background-color: #FFFFFF !important;
        color: #383031 !important;
        border-radius: 12px !important;
        padding: 15px !important;
        font-size: 16px !important;
        border: none !important;
        box-shadow: 0 2px 8px rgba(0,0,0,0.05);
    }

    [data-testid="stButton"] button {
        background-color: #D2C3F6 !important;
        color: #383031 !important;
        border-radius: 12px !important;
        padding: 10px 22px !important;
        font-size: 16px !important;
        font-weight: 600;
        transition: all 0.3s ease-in-out;
        box-shadow: 0px 4px 10px rgba(0,0,0,0.06);
        border: none;
    }

    [data-testid="stButton"] button:hover {
        background-color: #B9A9EC !important;
        transform: scale(1.02);
    }

    .custom-box {
        background-color: #F2EEFD;
        padding: 20px;
        border-radius: 16px;
        box-shadow: 0px 6px 14px rgba(0, 0, 0, 0.04);
        margin-bottom: 20px;
    }

    .stSuccess {
        background-color: #E7F9EF !important;
        border-radius: 12px !important;
        color: #355C47 !important;
    }

    .stError {
        background-color: #FFE9EC !important;
        border-radius: 12px !important;
        color: #A74449 !important;
    }

    .stInfo {
        background-color: #E9F0FF !important;
        border-radius: 12px !important;
        color: #3E5F88 !important;
    }

    h1, h2, h3 {
        color: #3D2E54 !important;
    }

    footer, header {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# Funcionalidad
translator = Translator()

st.markdown("<h1 style='text-align: center;'>🌸 Análisis de Sentimientos</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Explora la polaridad y subjetividad de tus textos con una reacción emocional suave y cálida.</p>", unsafe_allow_html=True)
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
    with st.container():
        st.markdown('<div class="custom-box">', unsafe_allow_html=True)

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
        
        st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.subheader("✍️ Corrector de inglés")
    with st.container():
        st.markdown('<div class="custom-box">', unsafe_allow_html=True)

        text2 = st.text_area("Escribe un texto en inglés para corregir:", key="correction")

        if text2:
            blob2 = TextBlob(text2)
            st.markdown("**Texto corregido:**")
            st.write(blob2.correct())

        st.markdown('</div>', unsafe_allow_html=True)

st.markdown("---")
st.caption("🎀 Desarrollado por Valentina • Powered by TextBlob & Google Translate")







