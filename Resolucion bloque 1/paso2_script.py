# BLOQUE I - PASO 2 (EJECUCIÓN)

import pandas as pd
import matplotlib.pyplot as plt

# Cargar datos
df = pd.read_csv("ventas_mayo_2026.csv")

# Copia limpia
df_clean = df.copy()

# Limpieza
df_clean["canal"] = df_clean["canal"].fillna("desconocido")
df_clean["importe"] = df_clean["importe"].fillna(df_clean["importe"].median())

# --- ANALISIS POR CANAL ---
resumen_canal = df_clean.groupby("canal").agg(
    ventas_totales=("importe","sum"),
    conversion_media=("descuento","mean")
).sort_values("conversion_media", ascending=False)

print("\nRESUMEN POR CANAL:")
print(resumen_canal)

# Identificar mejores
mejor_canal_conversion = resumen_canal.index[0]
mayor_ventas = resumen_canal["ventas_totales"].idxmax()

print("\nRESULTADOS:")
print("Mejor conversión:", mejor_canal_conversion)
print("Mayor volumen de ventas:", mayor_ventas)

# Grafico
plt.figure()
resumen_canal["ventas_totales"].plot(kind="bar")
plt.title("Ventas por canal")
plt.xticks(rotation=45)
plt.show()
