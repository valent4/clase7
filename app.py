import streamlit as st
from textblob import TextBlob
from googletrans import Translator

# Configuración de la página
st.set_page_config(page_title="Análisis de Sentimientos", layout="centered")

# Estilos personalizados con colores fríos pastel
st.markdown("""
    <style>
        body, .main, .stApp {
            background-color: #E8F4F8;  /* Fondo en azul pastel */
            color: #2E3A47;  /* Texto oscuro pero suave */
            font-family: 'Arial', sans-serif;
        }
        .stTextInput>div>div>input, textarea {
            background-color: #D1E7FF !important;  /* Fondo azul claro */
            color: #2E3A47 !important;  /* Texto oscuro */
            border-radius: 8px;
            padding: 10px;
        }
        .stButton>button {
            background-color: #A7C8F2;  /* Botón en azul pastel */
            color: white;
            border-radius: 12px;
            font-size: 16px;
            padding: 0.5em 1em;
        }
        .block-container {
            padding-top: 2rem;
        }
        .stTextArea textarea {
            background-color: #D1E7FF !important;  /* Fondo azul claro */
            color: #2E3A47 !important;  /* Texto oscuro */
            border-radius: 8px;
            padding: 10px;
        }
        .stMarkdown {
            color: #2E3A47;  /* Texto más oscuro para las frases */
        }
        h1, h2, h3 {
            color: #2E3A47;  /* Títulos en color oscuro */
        }
        .stSuccess {
            background-color: #D1F7E6;  /* Verde pastel suave */
            border: 1px solid #A4E6B0;
            color: #4C9F7F;
        }
        .stError {
            background-color: #FAD6D0;  /* Rosa pastel suave */
            border: 1px solid #F5A7A0;
            color: #D86F5A;
        }
        .stInfo {
            background-color: #D1ECF9;  /* Azul pastel claro */
            border: 1px solid #A6D9E9;
            color: #336A76;
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



