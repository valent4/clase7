from textblob import TextBlob
 from googletrans import Translator
 
 # Configuración básica
 # Configuración de la página
 st.set_page_config(page_title="Análisis de Sentimientos", layout="centered")
 
 # Estilos oscuros personalizados
 st.markdown("""
     <style>
         body, .main, .stApp {
             background-color: #121212;
             color: #E0E0E0;
         }
         .stTextInput>div>div>input, textarea {
             background-color: #1E1E1E !important;
             color: #E0E0E0 !important;
         }
         .stButton>button {
             background-color: #7B61FF;
             color: white;
             border-radius: 10px;
             font-size: 16px;
             padding: 0.5em 1em;
         }
         .block-container {
             padding-top: 2rem;
         }
         .stTextArea textarea {
             background-color: #1E1E1E !important;
             color: #E0E0E0 !important;
         }
     </style>
 """, unsafe_allow_html=True)
 
 translator = Translator()
 
 # Título principal
 st.title("Análisis de Sentimientos con TextBlob")
 # Título
 st.markdown("<h1 style='text-align: center;'>🧠 Análisis de Sentimientos</h1>", unsafe_allow_html=True)
 st.markdown("<p style='text-align: center;'>Analiza la polaridad y subjetividad de un texto y recibe una reacción emocional.</p>", unsafe_allow_html=True)
 
 # Introducción breve
 st.markdown("Analiza la polaridad y subjetividad de un texto de forma simple.")
 st.markdown("---")
 
 # Información lateral
 # Sidebar
 with st.sidebar:
     st.header("Información útil")
     st.header("ℹ️ ¿Qué mide esta app?")
     st.markdown("""
     **Polaridad**  
     Indica si el sentimiento del texto es positivo, negativo o neutral.  
     Rango: -1 (muy negativo) a 1 (muy positivo).
 
     Valor entre -1 (muy negativo) y 1 (muy positivo).  
     **Subjetividad**  
     Mide qué tan subjetivo (opiniones, emociones) u objetivo (hechos) es el texto.  
     Rango: 0 (objetivo) a 1 (subjetivo).
     Valor entre 0 (muy objetivo) y 1 (muy subjetivo).
     
     ---
     🧩 **Tip:** Escribe algo sincero para ver cómo reacciona la IA.
     """)
 
 st.markdown("---")
 
 # Crear las columnas
 # Columnas principales
 col1, col2 = st.columns(2)
 
 # Columna 1: Análisis de Polaridad y Subjetividad
 # Columna 1: Análisis de sentimientos
 with col1:
     st.subheader("Análisis de Polaridad y Subjetividad")
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
 
         st.markdown("**Resultados**")
         st.write("Polaridad:", polarity)
         st.write("Subjetividad:", subjectivity)
         # Mostrar resultados
         st.markdown("**Resultados del análisis:**")
         st.write("🔵 Polaridad:", polarity)
         st.write("🟡 Subjetividad:", subjectivity)
 
         # Respuesta emocional adaptada
         st.markdown("**🤖 Reacción del sistema:**")
         if polarity >= 0.5:
             st.write("Sentimiento: Positivo")
             st.success("¡Qué bonito lo que escribiste! Se siente muy positivo 🌟")
         elif polarity <= -0.5:
             st.write("Sentimiento: Negativo")
             st.error("Veo que hay sentimientos negativos... Si necesitas hablar, aquí estoy. 💙")
         else:
             st.write("Sentimiento: Neutral")
             st.info("Tu texto tiene un tono neutral. ¿Quieres contarme más? 🤔")
 
 # Columna 2: Corrector de texto en inglés
 # Columna 2: Corrector en inglés
 with col2:
     st.subheader("Corrección de texto en inglés")
     st.subheader("✏️ Corrector de texto en inglés")
     text2 = st.text_area("Escribe un texto en inglés para corregir:", key="correction")
 
     if text2:
         blob2 = TextBlob(text2)
         st.markdown("**Texto corregido:**")
         st.write(blob2.correct())
 
 # Pie de página discreto
 # Pie de página
 st.markdown("---")
 st.caption("Aplicación desarrollada como demostración del uso de TextBlob y Google Translate.")
 st.caption("💻 Desarrollado por Valentina • Powered by TextBlob & Google Translate")
 








