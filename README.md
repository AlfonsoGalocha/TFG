# 🎓 TFG - Sistema de Detección de Intrusos basado en Inteligencia Artificial

Este repositorio contiene el desarrollo del Trabajo de Fin de Grado (TFG) del Grado en Ingeniería Informática en la Universidad Camilo José Cela. El proyecto consiste en la creación de un sistema de detección de intrusos (IDS) que utiliza técnicas de inteligencia artificial para identificar amenazas y malware en tráfico de red, empleando el dataset **CICIDS2017**.

---

## 🎯 Objetivo del proyecto

Diseñar y construir un IDS inteligente capaz de:

- Analizar tráfico de red y extraer características relevantes.
- Clasificar automáticamente comportamientos normales y maliciosos.
- Detectar ciberataques usando algoritmos de aprendizaje automático.
- Evaluar el rendimiento del sistema a través de métricas como precisión, recall y F1-score.

---

## 📂 Dataset utilizado

El proyecto se basa en el dataset **CICIDS2017**, proporcionado por el Canadian Institute for Cybersecurity. Este dataset simula tráfico real en una red corporativa e incluye tanto tráfico benigno como múltiples tipos de ataques, como:

- DDoS
- PortScan
- Infiltration
- Web Attacks
- Botnet
- Brute Force

🔗 Más información: [CICIDS2017 - Canadian Institute for Cybersecurity](https://www.unb.ca/cic/datasets/ids-2017.html)

---

## ⚙️ Estructura del repositorio

- `LimpiezaDataset.ipynb`: Notebook con el preprocesamiento y limpieza del dataset.
- `analisisexploratorio.py`: Análisis exploratorio de las variables y la distribución de clases.
- `modelo_logisticareg.py`: Entrenamiento y evaluación del modelo de Regresión Logística.
- `modelo_randomforest.py`: Entrenamiento y evaluación del modelo Random Forest.
- `modelo_svm.py`: Entrenamiento y evaluación del modelo SVM (solo con subconjunto de datos).
- `*.pkl`: Archivos con los modelos entrenados exportados mediante joblib.

📝 **Nota:** Para generar los modelos `.pkl`, basta con **ejecutar las celdas** de los scripts correspondientes (pueden estar en formato notebook o script Python).

---

## 📈 Estado del desarrollo

- ✅ Limpieza y análisis del dataset
- ✅ Entrenamiento y evaluación de modelos
- ✅ Generación de modelos entrenados (`.pkl`)
- ✅ Comparación de resultados
- ✅ Documentación técnica

---

## 🧪 Cómo ejecutar el proyecto

1. Clona el repositorio:
```bash
git clone https://github.com/tuusuario/tfg-ids-ia.git
cd tfg-ids-ia
```

2. Instala las dependencias:
```bash
pip install -r requirements.txt
```

3. Ejecuta el preprocesamiento:
   - Abre `LimpiezaDataset.ipynb` y ejecuta todas las celdas.

4. Entrena modelos:
   - Ejecuta los notebooks o scripts correspondientes a cada modelo.

5. Evalúa resultados:
   - Revisa las métricas, gráficas y archivos `.pkl` generados.


## 📈 Resultados

| Modelo             | F1-score | AUC    | Tiempo por muestra |
|--------------------|----------|--------|---------------------|
| Random Forest      | 0.9999   | 1.0000 | 0.000004 s          |
| Regresión Logística| 0.9916   | 0.9992 | 0.000000 s          |
| SVM (10k muestras) | 0.8252   | 0.6713 | 0.000255 s          |


## 🔧 Entorno de desarrollo

- Python 3.10
- Jupyter Notebook (VS Code)
- `pandas`, `numpy`, `scikit-learn`, `matplotlib`, `seaborn`, `joblib`
- Ubuntu 22.04
- CPU x86_64, 4 núcleos / 8 hilos, 15 GB RAM


## 🧑‍💻 Autor

**Alfonso Galocha**  
Grado en Ingeniería Informática  
Universidad Camilo José Cela

---

## 📬 Contacto

📧 [alfonsogalocha@gmail.com] 
🔗 Proyecto desarrollado como parte del TFG, curso académico 2024-2025.


## 📄 Licencia

Proyecto con fines académicos como Trabajo de Fin de Grado. Sin licencia pública.
