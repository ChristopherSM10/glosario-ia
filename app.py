import os
from flask import Flask, render_template, request

app = Flask(__name__)


# ==========================================
# CONFIGURACIÓN Y DATOS DEL PROYECTO
# ==========================================
AUTOR = "Christopher Silverio"
TITULO_PROYECTO = "Glosario de Inteligencia Artificial"

glosario = [
    {
        "id": 1,
        "termino": "Big Data",
        "definicion": "Es el conjunto de grandes cantidades de datos que se generan y recopilan continuamente. En inteligencia artificial, estos datos pueden utilizarse para entrenar modelos y encontrar patrones que ayuden a realizar predicciones o tomar decisiones.",
        "fuente": "Stanford HAI. (s. f.). Artificial Intelligence Glossary.",
        "url": "https://hai.stanford.edu/ai-definitions"
    },
    {
        "id": 2,
        "termino": "Agentes de IA e IA agéntica",
        "definicion": "Un agente de IA es un programa de IA autónomo, puede realizar tareas y lograr objetivos en nombre de un usuario u otro sistema sin intervención humana, diseñando su propio flujo de trabajo y utilizando las herramientas disponibles (otras aplicaciones o servicios).\n\nLa IA agéntica es un sistema de múltiples agentes de IA, cuyos esfuerzos se coordinan u orquestan para lograr una tarea más compleja o un objetivo mayor que el que podría lograr cualquier agente individual en el sistema.",
        "fuente": "IBM. (2026). ¿Qué son los agentes de IA? | IBM Think.",
        "url": "https://www.ibm.com/mx-es/think/topics/ai-agents"
    },
    {
        "id": 3,
        "termino": "IA generativa",
        "definicion": "La IA generativa se refiere a modelos de aprendizaje profundo que pueden crear contenido original complejo, como texto extenso, imágenes de alta calidad, video o audio realistas y más, en respuesta a una instrucción o solicitud del usuario.",
        "fuente": "IBM. (2026). ¿Qué es la IA generativa? | IBM Think.",
        "url": "https://www.ibm.com/mx-es/think/topics/generative-ai"
    },
    {
        "id": 4,
        "termino": "Datos de entrenamiento",
        "definicion": "Son los datos utilizados para enseñar a un modelo de inteligencia artificial a reconocer patrones y realizar una determinada tarea. La calidad y variedad de estos datos pueden influir directamente en el funcionamiento del modelo.",
        "fuente": "Stanford HAI. (s. f.). Artificial Intelligence Glossary.",
        "url": "https://hai.stanford.edu/ai-definitions"
    },
    {
        "id": 5,
        "termino": "Alucinación de IA",
        "definicion": "Es cuando un sistema de inteligencia artificial genera información que parece correcta o convincente, pero que en realidad es falsa, incorrecta o no está respaldada por los datos disponibles.",
        "fuente": "Stanford HAI. (s. f.). Artificial Intelligence Glossary.",
        "url": "https://hai.stanford.edu/ai-definitions"
    },
    {
        "id": 6,
        "termino": "Algoritmo",
        "definicion": "Un algoritmo es un conjunto de instrucciones paso a paso para resolver un problema o completar una tarea, similar a una receta. En informática, los algoritmos indican a una computadora cómo procesar entradas, como datos, para producir una salida, como una decisión, predicción o lista ordenada. Algunos algoritmos son simples y fijos, mientras que otros pueden aprender patrones a partir de datos, como ocurre en el aprendizaje automático.",
        "fuente": "Stanford HAI. (s. f.). Artificial Intelligence Glossary.",
        "url": "https://hai.stanford.edu/ai-definitions"
    },
    {
        "id": 7,
        "termino": "IA multimodal",
        "definicion": "Es un tipo de inteligencia artificial capaz de procesar y combinar diferentes tipos de información, como texto, imágenes, audio y video, para comprender información y generar respuestas.",
        "fuente": "Stanford HAI. (s. f.). Artificial Intelligence Glossary.",
        "url": "https://hai.stanford.edu/ai-definitions"
    },
    {
        "id": 8,
        "termino": "Sesgo en IA",
        "definicion": "Ocurre cuando un sistema de inteligencia artificial produce resultados que favorecen o perjudican injustamente a ciertos grupos de personas. Puede originarse por datos de entrenamiento que contienen prejuicios históricos, por una representación desigual de los grupos o por la forma en que se diseña y evalúa el sistema.",
        "fuente": "Stanford HAI. (s. f.). Artificial Intelligence Glossary.",
        "url": "https://hai.stanford.edu/ai-definitions"
    },
    {
        "id": 9,
        "termino": "Machine Learning (Aprendizaje automático)",
        "definicion": "Es un subconjunto de la inteligencia artificial que permite a las computadoras aprender patrones a partir de datos y realizar predicciones o tomar decisiones sin recibir instrucciones específicas para cada situación.",
        "fuente": "IBM. (s. f.). ¿Qué es el machine learning? | IBM Think.",
        "url": "https://www.ibm.com/mx-es/think/topics/machine-learning"
    },
    {
        "id": 10,
        "termino": "Deep Learning (Aprendizaje profundo)",
        "definicion": "Es un tipo de machine learning que utiliza redes neuronales con múltiples capas para aprender patrones complejos a partir de grandes cantidades de datos.",
        "fuente": "IBM. (s. f.). ¿Qué es el aprendizaje profundo? | IBM Think.",
        "url": "https://www.ibm.com/mx-es/think/topics/deep-learning"
    },
    {
        "id": 11,
        "termino": "Redes neuronales",
        "definicion": "Son modelos de machine learning formados por capas de neuronas artificiales que aprenden patrones de los datos para relacionar entradas con resultados.",
        "fuente": "IBM. (s. f.). ¿Qué son las redes neuronales? | IBM Think.",
        "url": "https://www.ibm.com/mx-es/think/topics/neural-networks"
    },
    {
        "id": 12,
        "termino": "Procesamiento del lenguaje natural (PLN)",
        "definicion": "Es un campo de la inteligencia artificial que permite a las computadoras comprender, procesar y comunicarse mediante el lenguaje humano, tanto escrito como hablado.",
        "fuente": "IBM. (s. f.). ¿Qué es el procesamiento de lenguaje natural (PLN)? | IBM Think.",
        "url": "https://www.ibm.com/mx-es/think/topics/natural-language-processing"
    },
    {
        "id": 13,
        "termino": "Visión artificial",
        "definicion": "Es un subcampo de la inteligencia artificial que permite a las máquinas procesar, analizar e interpretar información visual, como imágenes y videos.",
        "fuente": "IBM. (s. f.). ¿Qué es la visión artificial? | IBM Think.",
        "url": "https://www.ibm.com/mx-es/think/topics/computer-vision"
    },
    {
        "id": 14,
        "termino": "Aprendizaje supervisado",
        "definicion": "Es un tipo de machine learning en el que un modelo aprende utilizando datos de entrenamiento que contienen ejemplos y sus respuestas correctas. De esta manera, puede aprender a realizar predicciones sobre nuevos datos.",
        "fuente": "Google for Developers. (s. f.). Machine Learning Glossary.",
        "url": "https://developers.google.com/machine-learning/glossary"
    },
    {
        "id": 15,
        "termino": "Aprendizaje no supervisado",
        "definicion": "Es un tipo de machine learning que permite a un modelo encontrar patrones, relaciones o grupos dentro de datos que no tienen respuestas previamente etiquetadas.",
        "fuente": "IBM. (s. f.). ¿Qué es el machine learning? | IBM Think.",
        "url": "https://www.ibm.com/mx-es/think/topics/machine-learning"
    },
    {
        "id": 16,
        "termino": "Aprendizaje por refuerzo",
        "definicion": "Es un tipo de machine learning en el que un modelo aprende a tomar decisiones evaluando su entorno y seleccionando acciones que buscan obtener la mayor recompensa posible.",
        "fuente": "IBM. (s. f.). ¿Qué es el machine learning? | IBM Think.",
        "url": "https://www.ibm.com/mx-es/think/topics/machine-learning"
    },
    {
        "id": 17,
        "termino": "Modelo de IA",
        "definicion": "Es una estructura matemática o computacional que procesa datos de entrada para generar resultados, como predicciones, decisiones o clasificaciones. Los modelos se entrenan con datos para aprender patrones y realizar determinadas tareas.",
        "fuente": "Google for Developers. (s. f.). Machine Learning Glossary.",
        "url": "https://developers.google.com/machine-learning/glossary"
    },
    {
        "id": 18,
        "termino": "Ética de la IA",
        "definicion": "Es un campo multidisciplinario que busca aumentar los beneficios de la inteligencia artificial y reducir sus riesgos y resultados negativos. También analiza aspectos como la justicia, la transparencia, la privacidad y la responsabilidad en el uso de sistemas de IA.",
        "fuente": "IBM. (s. f.). ¿Qué es la ética de la IA? | IBM Think.",
        "url": "https://www.ibm.com/mx-es/think/topics/ai-ethics"
    },
    {
        "id": 19,
        "termino": "Modelo de lenguaje grande (LLM)",
        "definicion": "Es un tipo de modelo de inteligencia artificial entrenado con grandes cantidades de texto para comprender y generar lenguaje humano. Puede utilizarse para tareas como responder preguntas, resumir textos, traducir y generar contenido.",
        "fuente": "Stanford Medicine. (s. f.). Brief glossary of artificial intelligence (AI) terms.",
        "url": "https://stanmed.stanford.edu/brief-glossary-artificial-intelligence-ai/"
    },
    {
        "id": 20,
        "termino": "IA multimodal (Avanzada)",
        "definicion": "Es un tipo de inteligencia artificial capaz de procesar y combinar diferentes tipos de información, como texto, imágenes, audio y video, para comprender una situación y generar respuestas.",
        "fuente": "Stanford HAI. (s. f.). Artificial Intelligence Glossary.",
        "url": "https://hai.stanford.edu/ai-definitions"
    },
   {
        "id": 21,
        "termino": "Sistema Inteligente",
        "definicion": """Un Sistema Inteligente es una entidad computacional autónoma capaz de percibir su entorno mediante sensores, procesar e interpretar dicha información a través de algoritmos de Inteligencia Artificial (como aprendizaje automático, redes neuronales o sistemas basados en reglas), y tomar decisiones fundamentadas para ejecutar acciones a través de actuadores con el fin de alcanzar objetivos específicos. A diferencia de los sistemas de software tradicionales, un sistema inteligente posee capacidad de adaptación, razonamiento y aprendizaje continuo a partir de la experiencia y los datos que recolecta en tiempo real.
        
        <div style="margin-top: 25px; text-align: center; width: 100%;">
            <p style="color: #38bdf8; font-weight: bold; margin-bottom: 12px; font-size: 1rem;">📌 Esquema Básico de un Sistema Inteligente</p>
            <div style="background: #ffffff; padding: 12px; border-radius: 12px; display: block; margin: 0 auto; max-width: 650px; box-shadow: 0 4px 15px rgba(0, 0, 0, 0.4);">
                <img src="/static/esquema_sistema_inteligente.png" alt="Esquema Básico de Sistema Inteligente" style="width: 100%; height: auto; max-height: 500px; object-fit: contain; border-radius: 8px; display: block; margin: 0 auto;">
            </div>
        </div>""",
        "fuente": "Russell, S., & Norvig, P. (2020). Artificial Intelligence: A Modern Approach.",
        "url": "https://aima.cs.berkeley.edu/"
    }
]

# ==========================================
# RUTAS DE LA APLICACIÓN
# ==========================================
@app.route("/", methods=["GET", "POST"])
def inicio():
    busqueda = request.form.get("busqueda", "").strip().lower()
    
    if busqueda:
        resultados = [
            c for c in glosario
            if busqueda in c["termino"].lower() or busqueda in c["definicion"].lower()
        ]
    else:
        resultados = glosario

    return render_template(
        "index.html",
        titulo=TITULO_PROYECTO,
        autor=AUTOR,
        conceptos=resultados,
        total=len(glosario),
        busqueda=busqueda
    )
@app.route('/etica')
def etica():
    return render_template('etica.html')

@app.route('/ejemplo-ml')
def ejemplo_ml():
    return render_template('ejemplo_ml.html')

if __name__ == '__main__':
    print("🚀 Iniciando servidor Flask...")
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)