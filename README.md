# 🎓 TFG - Sistema de Detección de Intrusos basado en Inteligencia Artificial

Este repositorio contiene el desarrollo del Trabajo de Fin de Grado (TFG) del Grado en Ingeniería Informática en la Universidad Camilo José Cela. El proyecto consiste en la creación de un sistema de detección de intrusos (IDS) que utiliza técnicas de inteligencia artificial para identificar amenazas y malware en tráfico de red, empleando el dataset **CICIDS2017**.

---

## 🎯 Objetivo del proyecto

Diseñar y construir un IDS inteligente capaz de:

- Analizar tráfico de red y extraer características relevantes.
- Clasificar automáticamente comportamientos normales y maliciosos.
- Detectar diversos tipos de ciberataques usando algoritmos de aprendizaje automático.
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

- `LimpiezaDataset.ipynb`: Preprocesamiento y limpieza de los datos.
- `analisisexploratorio.ipynb`: Análisis exploratorio inicial del dataset.
- `LogisticRegression.ipynb`: Entrenamiento, evaluación y guardado del modelo de regresión logística en `logistic_regression_model.pkl`.
- `modelo_randomforest.ipynb`: Entrenamiento, evaluación y guardado del modelo Random Forest en `modelo_randomforest.pkl`.

📝 **Nota:** Para generar los modelos `.pkl`, basta con **ejecutar las celdas** de los scripts correspondientes (pueden estar en formato notebook o script Python).

---

## 📈 Estado del desarrollo

- ✅ Limpieza y consolidación del dataset
- ✅ Análisis exploratorio
- ✅ Implementación y evaluación de modelos: regresión logística y random forest
- ✅ Generación de modelos entrenados (`.pkl`)
- ✅ Documentación del proyecto actualizada
- Modelo SVM desarrollar y documentar
- Comparacion entre modelos 
---

## 🧑‍💻 Autor

**Alfonso Galocha**  
Grado en Ingeniería Informática  
Universidad Camilo José Cela

---

## 📬 Contacto

📧 [alfonsogalocha@gmail.com] 
🔗 Proyecto desarrollado como parte del TFG, curso académico 2024-2025.
