import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.neighbors import NearestNeighbors
import matplotlib.pyplot as plt
import seaborn as sns


# -------------------- 1. CARGA Y LIMPIEZA DE DATOS --------------------

# Cargar datos
df = pd.read_csv("FastFoodNutritionMenuV3.csv")
print(df)

# Limpiar nombres de columnas
df.columns = df.columns.str.replace(r'\s+|\n', ' ', regex=True).str.strip()

# Selección de columnas numéricas
nutrient_cols = [
    'Calories', 'Total Fat (g)', 'Saturated Fat (g)', 'Trans Fat (g)',
    'Cholesterol (mg)', 'Sodium (mg)', 'Carbs (g)', 'Fiber (g)',
    'Sugars (g)', 'Protein (g)'
]