import streamlit as st
from textblob import TextBlob
from googletrans import Translator

# Configuración de la página
st.set_page_config(page_title="Análisis de Sentimientos", layout="centered")

# Estilos para fondo claro y texto oscuro
st.markdown("""
    <style>
        body, .main, .stApp {
            background-color: #F4E1F4; /* Fondo morado claro */
            color: #4B0082; /* Texto morado oscuro para contraste */
        }
        .stTextInput>div>div>input, textarea {
            background-color: #E0B0FF !important; /* Fondo morado pastel */
            color: #4B0082 !important; /* Texto morado oscuro */
            border-radius: 8px;
        }
        .stButton>button {
            background-color: #FFB6C1; /* Rosa pastel */
            color: #4B0082; /* Texto morado oscuro */
            border-radius: 12px;
            font-size: 16px;
            padding: 0.5em 1em;
        }
        .block-container {
            padding-top: 2rem;
        }
        .stTextArea textarea {
            background-color: #E0B0FF !important; /* Fondo morado pastel */
            color: #4B0082 !important; /* Texto morado oscuro */
            border-radius: 8px;
        }
        h1 {
            color: #9B4D96; /* Morado medio para el título */
        }
        .stMarkdown {
            font-size: 16px;
            color: #4B0082; /* Morado oscuro */
        }
    </style>
""", unsafe_allow_html=True)

translator = Translator()

# Título
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
        # Traducir a inglés para análisis con TextBlob
        translation = translator.translate(text1, src="es", dest="en")
        translated_text = translation.text
        blob = TextBlob(translated_text)

        # Obtener polaridad y subjetividad
        polarity = round(blob.sentiment.polarity, 2)
        subjectivity = round(blob.sentiment.subjectivity, 2)

        # Mostrar resultados
        st.markdown("**Resultados del análisis:**")
        st.write("🔵 Polaridad:", polarity)
        st.write("🟡 Subjetividad:", subjectivity)

        # Respuesta emocional adaptada
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






