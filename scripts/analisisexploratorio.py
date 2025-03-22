import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar el dataset limpio
file_path = "cleaned_dataset.csv"  # Asegúrate de cambiar la ruta si es necesario
df = pd.read_csv(file_path)

# Configurar estilo de los gráficos
sns.set(style="whitegrid")

# 1️⃣ Información general del dataset
print("### Información del dataset:")
print(df.info())

# 2️⃣ Resumen estadístico
print("\n### Resumen estadístico del dataset:")
print(df.describe())

# 3️⃣ Distribución de la variable objetivo (Label)
plt.figure(figsize=(6, 4))
sns.countplot(x=df["Label"], palette="viridis")
plt.title("Distribución de tráfico benigno vs. tráfico malicioso")
plt.xlabel("Clase (0 = Benigno, 1 = Malicioso)")
plt.ylabel("Cantidad de muestras")
plt.show()

# 4️⃣ Matriz de correlación entre variables numéricas
plt.figure(figsize=(12, 8))
correlation_matrix = df.corr()
sns.heatmap(correlation_matrix, cmap="coolwarm", annot=False, linewidths=0.5)
plt.title("Matriz de correlación entre características")
plt.show()

# 5️⃣ Distribución de algunas características clave
fig, axes = plt.subplots(1, 3, figsize=(18, 5))

sns.histplot(df["Flow Duration"], bins=50, kde=True, ax=axes[0])
axes[0].set_title("Distribución de Flow Duration")

sns.histplot(df["Total Fwd Packets"], bins=50, kde=True, ax=axes[1])
axes[1].set_title("Distribución de Total Fwd Packets")

sns.histplot(df["Total Backward Packets"], bins=50, kde=True, ax=axes[2])
axes[2].set_title("Distribución de Total Backward Packets")

plt.tight_layout()
plt.show()
