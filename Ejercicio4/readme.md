# 🌾 Machine Learning para Agricultura de Precisión: Monitoreo de Salud de Cultivos IoT

Este repositorio contiene un ejercicio práctico basado en un **dataset real de sensores IoT agrícolas** (`Plant_health_data.csv`, obtenido de Kaggle por *gowthamduggirala*). El proyecto replica el flujo de trabajo completo de un científico de datos aplicado al sector agroindustrial.

---

## 📊 Sobre el Dataset

* **Registros:** 1,200 muestras.
* **Columnas:** 14 variables en total.
* **Variables predictoras (10 sensores numéricos):** Humedad del suelo, temperatura ambiente y de suelo, humedad relativa del aire, intensidad lumínica, pH del suelo, niveles de nitrógeno ($N$), fósforo ($P$) y potasio ($K$), contenido de clorofila y una señal electroquímica (utilizada como proxy de conductividad eléctrica).
* **Variable objetivo (`Plant_Health_Status`):** Predicción del estado de salud del cultivo dividida en tres categorías:
  * `Healthy` (Saludable)
  * `Moderate Stress` (Estrés moderado)
  * `High Stress` (Estrés alto)

---

## 📓 Estructura del Notebook (`Cultivating_ML.ipynb`)

El notebook está organizado en **8 sesiones incrementales**, donde el código de cada sección da continuidad al anterior:

* **Sesión 1:** Carga y estructura del dato rectangular.
* **Sesión 2:** Estadística descriptiva y limpieza robusta con imputación por mediana.
* **Sesión 3:** Análisis exploratorio de datos (histogramas y matriz de correlación de Pearson).
* **Sesión 4:** Transformación logarítmica y escala de potencias de Tukey para linealizar sensores con cola larga.
* **Sesión 5:** Partición estratificada 80/20 y estandarización Z-score sin fuga de datos (*data leakage*).
* **Sesión 6:** Modelado comparativo entre Regresión Logística y Árbol de Decisión CART.
* **Sesión 7:** Modelos de ensamblaje (*Random Forest* y *XGBoost*) con validación cruzada e importancia de variables.
* **Sesión 8:** Pipeline consolidado, tabla comparativa de los 4 modelos, matriz de confusión y reporte de clasificación del mejor modelo.

---

## ⚙️ Requisitos Previos y Configuración en Google Colab

Antes de ejecutar el notebook en Colab, asegúrate de contar con tus credenciales de la API de Kaggle:

1. Dirígete a tu cuenta de Kaggle en **Settings > API > Create New Token**.
2. Descarga el archivo de credenciales (`kaggle.json`).
3. Sube el archivo cuando la primera celda del notebook lo solicite. Esta celda se encargará de descargar automáticamente el dataset real directamente a la carpeta `./data`.

---

## ❓ Preguntas Prácticas para el Análisis

Para profundizar en el desarrollo del proyecto, responde y analiza los siguientes puntos a lo largo de las sesiones:

* **Sesión 2:** ¿Qué sensor muestra la mayor diferencia entre su media y su mediana? ¿Qué indica esto sobre la presencia de *outliers* producidos por fallos de sensor?
* **Sesión 3:** ¿Qué par de sensores tiene la correlación de Pearson más alta (en valor absoluto) y cuál la más cercana a cero? Interpreta ambos casos.
* **Sesión 4:** Aplica la transformación logarítmica a otro sensor con distribución sesgada (por ejemplo, `Potassium_Level`) y evalúa si mejora alguna correlación de interés.
* **Sesión 5:** Quita el parámetro `stratify=y` del `train_test_split` y observa cuántos registros de la clase *"High Stress"* quedan en el conjunto de prueba.
* **Sesión 6:** Cambia el hiperparámetro `max_depth` del árbol CART a `2` y posteriormente a `10`. Relaciona los cambios en el puntaje **F1-macro** con el concepto de sobreajuste (*overfitting*).
* **Sesión 7:** Identifica los 3 sensores con mayor importancia en tu corrida experimental y propón una justificación o explicación agronómica.
* **Sesión 8:** Con base en tus propios resultados, concluye razonadamente **qué modelo desplegarías en campo**, sopesando tanto el rendimiento global (**F1-macro**) como la capacidad de detección oportuna (**recall** de la clase *"High Stress"*).
