Análisis de Datos de Enfermedad Cardíaca

Análisis exploratorio de datos (EDA) de un dataset de enfermedades cardíacas para identificar patrones y factores de riesgo.

📊 Descripción del Proyecto

Este proyecto realiza un análisis completo de datos médicos relacionados con enfermedades cardíacas, transformando un notebook Jupyter en un script ejecutable de Python. El análisis incluye limpieza de datos, visualizaciones y detección de valores atípicos médicamente imposibles.

🎯 Objetivos

Explorar y entender la estructura del dataset de enfermedades cardíacas

Limpiar datos médicamente imposibles (valores cero en presión arterial y colesterol)

Analizar variables sensibles como edad y género

Visualizar relaciones entre variables y la enfermedad cardíaca

Crear un script reproducible para análisis de datos médicos

🚀 Características Principales

✅ Análisis de Calidad de Datos: Detección de valores nulos, duplicados y uso de memoria

✅ Estadísticas Descriptivas: Resúmenes numéricos completos para todas las variables

✅ Visualizaciones Profesionales: Gráficos de distribución y análisis de variables sensibles

✅ Limpieza de Datos Médicos: Eliminación de valores imposibles (presión arterial = 0, colesterol = 0)

✅ Análisis de Variables Sensibles: Estudio de distribución por edad y género

✅ Script Ejecutable: Conversión completa de notebook Jupyter a script Python

🛠️ Tecnologías Utilizadas

Tecnología	Versión	Uso

Python	3.8+	Lenguaje de programación principal
Pandas	≥1.3.0	Manipulación y análisis de datos
NumPy	≥1.20.0	Cálculos numéricos
Matplotlib	≥3.3.0	Visualizaciones básicas
Seaborn	≥0.11.0	Visualizaciones estadísticas
Jupyter	≥1.0.0	Desarrollo inicial del análisis

📁 Estructura del Proyecto
text
heart-disease-analysis/
├── 📄 heart_disease_analysis.py    # Script principal de análisis
├── 📄 requirements.txt              # Dependencias del proyecto
├── 📄 README.md                     # Documentación completa
├── 📊 heart.csv                     # Dataset original
├── 📈 analisis_variables_sensibles.png  # Gráfico generado
└── 📊 impacto_limpieza_datos.png        # Gráfico generado

⚡ Instalación y Uso Rápido

Prerrequisitos
Python 3.8 o superior

pip (gestor de paquetes de Python)

Pasos de Instalación
Descarga el proyecto

# Opción 1: Clona el repositorio (si usas Git)
git clone https://github.com/tu-usuario/heart-disease-analysis.git

# Opción 2: Descarga manual los archivos
# - heart_disease_analysis.py
# - requirements.txt
# - heart.csv
Instala las dependencias

pip install -r requirements.txt
Ejecuta el análisis

python heart_disease_analysis.py

🎮 Uso del Script

El script ejecutará automáticamente todo el análisis:

# Ejecutar análisis completo
python heart_disease_analysis.py

# Salida esperada:
✅ Librerías importadas correctamente
📥 Cargando dataset heart.csv...
✅ Dataset cargado correctamente
📊 Dimensiones del dataset: (918, 12)
...

📈 Resultados y Hallazgos

Análisis de Datos
Dataset original: 918 registros, 12 características

Variables categóricas: Sexo, Tipo de Dolor Torácico, ECG en Reposo, etc.

Variables numéricas: Edad, Presión Arterial, Colesterol, Frecuencia Cardíaca Máxima, etc.

Limpieza de Datos
Registros eliminados: 172 (valores médicamente imposibles)

Dataset limpio: 746 registros (81.3% conservado)

Verificación: Presión arterial mínima 92, Colesterol mínimo 85

Visualizaciones Generadas
Análisis de Variables Sensibles: Distribución por edad y género

Impacto de Limpieza: Comparación antes/después de la limpieza

🔍 Variables Analizadas
Variable	Tipo	Descripción
Age	Numérica	Edad del paciente
Sex	Categórica	Género (M/F)
ChestPainType	Categórica	Tipo de dolor torácico
RestingBP	Numérica	Presión arterial en reposo
Cholesterol	Numérica	Colesterol sérico
FastingBS	Numérica	Azúcar en ayunas
RestingECG	Categórica	Resultados ECG en reposo
MaxHR	Numérica	Frecuencia cardíaca máxima
ExerciseAngina	Categórica	Angina inducida por ejercicio
Oldpeak	Numérica	Depresión del segmento ST
ST_Slope	Categórica	Pendiente del segmento ST
HeartDisease	Binaria	Presencia de enfermedad cardíaca
🎨 Personalización
Puedes modificar el script para:

Agregar más visualizaciones: Edita la sección de gráficos

Cambiar umbrales de limpieza: Modifica los criterios de valores imposibles

Incluir análisis estadísticos: Añade tests de hipótesis

Exportar resultados: Guarda tablas resumen en CSV/Excel

# Ejemplo: Modificar umbral de limpieza
df_clean = df_clean[(df_clean['RestingBP'] > 90) & (df_clean['Cholesterol'] > 100)]
🤝 Contribuciones

¡Las contribuciones son bienvenidas! Si quieres mejorar este proyecto:

Haz fork del repositorio

Crea una rama para tu feature (git checkout -b feature/nueva-caracteristica)

Commit tus cambios (git commit -am 'Agrega nueva característica')

Push a la rama (git push origin feature/nueva-caracteristica)

Abre un Pull Request

Mejoras Posibles

Implementar machine learning para predicción

Crear dashboard interactivo

Análisis de correlaciones avanzado

Tests estadísticos adicionales

📝 Licencia

Este proyecto está bajo la Licencia MIT - ver el archivo LICENSE para detalles.

👨‍💻 Autor

Sebastián Rojas

GitHub: @sebastian-rojas

LinkedIn: Sebastián Rojas

Portafolio: tu-portafolio.com

🙏 Agradecimientos

Dataset: Heart Failure Prediction

Comunidad de Data Science

Documentación de pandas, matplotlib y seaborn