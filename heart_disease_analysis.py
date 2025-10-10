# heart_disease_analysis.py
# Análisis de Datos de Enfermedad Cardíaca
# Script convertido desde Jupyter Notebook para portafolio GitHub

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

print("✅ Librerías importadas correctamente")

def main():
    # Paso 1: Carga del dataset
    print("📥 Cargando dataset heart.csv...")
    
    try:
        df = pd.read_csv('heart.csv')
        print("✅ Dataset cargado correctamente")
        print(f"📊 Dimensiones del dataset: {df.shape}")
    except FileNotFoundError:
        print("❌ Archivo 'heart.csv' no encontrado en el directorio actual")
        print("📁 Por favor, asegúrate de que el archivo esté en la misma carpeta que este script")
        return
    
    # Información básica del dataset
    print("\n=== INFORMACIÓN DEL DATASET ===")
    print(f"📏 Dimensiones: {df.shape}")
    print(f"📋 Columnas: {df.columns.tolist()}")
    print("\n=== TIPOS DE DATOS ===")
    print(df.dtypes)
    
    # Análisis de calidad de datos
    print("\n=== ANÁLISIS DE CALIDAD DE DATOS ===")
    print("🔍 Valores nulos por columna:")
    print(df.isnull().sum())
    print(f"\n🔍 Filas duplicadas: {df.duplicated().sum()}")
    print(f"\n💾 Uso de memoria: {df.memory_usage(deep=True).sum() / 1024 ** 2:.2f} MB")
    
    # Análisis de variables categóricas
    print("\n=== VARIABLES CATEGÓRICAS ===")
    categorical_columns = df.select_dtypes(include=['object']).columns
    print(f"Columnas categóricas: {list(categorical_columns)}")
    
    for col in categorical_columns:
        print(f"\n📊 Distribución de '{col}':")
        print(df[col].value_counts())
    
    # Análisis de variables numéricas
    print("\n=== VARIABLES NUMÉRICAS ===")
    numeric_columns = df.select_dtypes(include=[np.number]).columns
    print(f"Columnas numéricas: {list(numeric_columns)}")
    print("\n📈 Estadísticas descriptivas:")
    print(df[numeric_columns].describe())
    
    # Análisis de variables sensibles
    print("\n=== VARIABLES SENSIBLES ===")
    sensitive_vars = ['Sex', 'Age']
    
    print("🔍 Análisis de variables sensibles:")
    for var in sensitive_vars:
        if var in df.columns:
            print(f"\n📋 Variable: {var}")
            if df[var].dtype == 'object':
                print(f"   Distribución:\n{df[var].value_counts()}")
            else:
                print(f"   Rango: {df[var].min()} - {df[var].max()}")
                print(f"   Media: {df[var].mean():.2f}")
            
            if 'HeartDisease' in df.columns:
                print(f"   Tasa de enfermedad cardiaca por categoría:")
                if df[var].dtype == 'object':
                    print(df.groupby(var)['HeartDisease'].mean().round(3))
                else:
                    correlation = df[var].corr(df['HeartDisease'])
                    print(f"   Correlación con HeartDisease: {correlation:.3f}")
    
    # Visualización de variables sensibles
    print("\n=== VISUALIZACIÓN DE VARIABLES SENSIBLES ===")
    fig, axes = plt.subplots(1, 2, figsize=(15, 5))
    
    if 'Sex' in df.columns and 'HeartDisease' in df.columns:
        pd.crosstab(df['Sex'], df['HeartDisease'], normalize='index').plot(
            kind='bar', ax=axes[0], title='Tasa de Enfermedad Cardiaca por Sexo'
        )
        axes[0].set_ylabel('Proporción')
    
    if 'Age' in df.columns and 'HeartDisease' in df.columns:
        df.boxplot(column='Age', by='HeartDisease', ax=axes[1])
        axes[1].set_title('Distribución de Edad por Enfermedad Cardiaca')
    
    plt.suptitle('Análisis de Variables Sensibles')
    plt.tight_layout()
    plt.savefig('analisis_variables_sensibles.png', dpi=300, bbox_inches='tight')
    plt.show()
    
    # Limpieza de datos - Eliminación de valores médicamente imposibles
    print("\n=== ELIMINACIÓN DE VALORES MÉDICAMENTE IMPOSIBLES ===")
    df_clean = df.copy()
    print("📊 Tamaño inicial del dataset:", df_clean.shape)
    
    invalid_restingbp = (df_clean['RestingBP'] == 0)
    invalid_cholesterol = (df_clean['Cholesterol'] == 0)
    
    print(f"🔍 Registros con RestingBP = 0: {invalid_restingbp.sum()}")
    print(f"🔍 Registros con Cholesterol = 0: {invalid_cholesterol.sum()}")
    
    # Eliminar registros con valores imposibles
    initial_count = len(df_clean)
    df_clean = df_clean[(df_clean['RestingBP'] > 0) & (df_clean['Cholesterol'] > 0)]
    removed_count = initial_count - len(df_clean)
    
    print(f"\n🗑️ Se eliminaron {removed_count} registros inválidos")
    print(f"📊 Tamaño final del dataset: {df_clean.shape}")
    print(f"📊 Porcentaje de datos conservados: {(len(df_clean)/initial_count*100):.1f}%")
    
    # Verificación final
    print("\n✅ Verificación final:")
    print(f"RestingBP mínimo: {df_clean['RestingBP'].min()}")
    print(f"Cholesterol mínimo: {df_clean['Cholesterol'].min()}")
    
    # Análisis del impacto de la limpieza
    print("\n=== ANÁLISIS DEL IMPACTO ===")
    fig, axes = plt.subplots(1, 2, figsize=(15, 5))
    
    # Antes de la limpieza
    axes[0].hist(df['RestingBP'], bins=30, alpha=0.7, color='red', label='Original')
    axes[0].set_title('Distribución de RestingBP (Original)')
    axes[0].set_xlabel('RestingBP')
    axes[0].set_ylabel('Frecuencia')
    
    # Después de la limpieza
    axes[1].hist(df_clean['RestingBP'], bins=30, alpha=0.7, color='green', label='Limpio')
    axes[1].set_title('Distribución de RestingBP (Limpio)')
    axes[1].set_xlabel('RestingBP')
    axes[1].set_ylabel('Frecuencia')
    
    plt.tight_layout()
    plt.savefig('impacto_limpieza_datos.png', dpi=300, bbox_inches='tight')
    plt.show()
    
    print("\n🎯 Análisis completado exitosamente!")
    print("📈 Gráficas guardadas como:")
    print("   - analisis_variables_sensibles.png")
    print("   - impacto_limpieza_datos.png")

if __name__ == "__main__":
    main()