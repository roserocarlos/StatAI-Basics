# 🌾 Machine Learning para Agricultura de Precisión: Monitoreo de Salud de Cultivos IoT

Este repositorio contiene un ejercicio práctico basado en un **dataset real de sensores IoT agrícolas** (`Plant_health_data.csv`, obtenido de Kaggle por *gowthamduggirala*). El proyecto replica el flujo de trabajo completo de un científico de datos aplicado al sector agroindustrial.

---

## 📊 Sobre el Dataset

* **Registros:** 1,200 muestras (10 plantas × 120 lecturas cada una, cada 6 horas).
* **Columnas:** 14 variables en total.
* **Variables predictoras (10 sensores numéricos, `SENSORES_NUM`):** humedad del suelo, temperatura ambiente y de suelo, humedad relativa del aire, intensidad lumínica, pH del suelo, niveles de nitrógeno (N), fósforo (P) y potasio (K), y una señal electroquímica (proxy de conductividad eléctrica).
* **Otras columnas del dataset (no son predictoras):** `Timestamp` y `Plant_ID` (identificadores), y `Chlorophyll_Content` — esta última no se usa como predictor del modelo; solo aparece en la Sesión 4 como variable de comparación al probar la transformación logarítmica.
* **Variable objetivo (`Plant_Health_Status`):** predicción del estado de salud del cultivo en tres categorías:
  * `Healthy` (Saludable)
  * `Moderate Stress` (Estrés moderado)
  * `High Stress` (Estrés alto)

---

## 📓 Estructura del Notebook (`Cultivating_ML.ipynb`)

El notebook está organizado en **8 sesiones incrementales**: el código de cada una da continuidad a la anterior, y dentro de cada sesión el trabajo está partido en bloques cortos (uno por tarea), cada uno con una línea de texto explicando qué hace, seguidos de una celda corta de "visualización de apoyo" y el ejercicio de cierre.

* **Sesión 1:** carga del CSV (detección insensible a mayúsculas/minúsculas) y estructura del dato rectangular.
* **Sesión 2:** estadística descriptiva (media, mediana, moda) y limpieza **según el origen físico de cada sensor** — interpolación dentro de la serie temporal de cada planta para los sensores que siguen un proceso direccional (humedad de suelo, luz, temperatura ambiente, humedad relativa), y mediana global para los que cambian más lento (pH, N, P, K). No se impone una sola estrategia de limpieza para todos los sensores por igual.
* **Sesión 3:** análisis exploratorio — correlación de Pearson entre sensores, **boxplots por clase y ANOVA F-test** para ver qué sensores distinguen realmente los 3 niveles de salud (antes de entrenar cualquier modelo), e histograma de `Light_Intensity`.
* **Sesión 4:** transformación logarítmica (`log10(x+1)`) como técnica de linealización de Tukey. En este dataset en particular, el sesgo (`skew`) de los 10 sensores es cercano a 0, así que el transform casi no cambia las correlaciones — un resultado real y honesto, no forzado — y por eso no se lleva la versión transformada al modelado final.
* **Sesión 5:** partición estratificada 80/20 y estandarización Z-score, ajustando el `scaler` solo con el conjunto de entrenamiento (sin fuga de datos).
* **Sesión 6:** modelado comparativo entre Regresión Logística y Árbol de Decisión CART.
* **Sesión 7:** modelos de ensamblaje (Random Forest y XGBoost) con validación cruzada e importancia de variables.
* **Sesión 8:** pipeline consolidado, tabla comparativa de los 4 modelos, matriz de confusión y reporte de clasificación del mejor modelo.

---

## ⚙️ Requisitos Previos y Configuración en Google Colab

Este notebook **no usa la API de Kaggle** (no hace falta `kaggle.json`). El archivo se sube manualmente:

1. Descarga `Plant_health_data.csv` desde [Kaggle](https://www.kaggle.com/datasets/gowthamduggirala/plant-health-data) a tu computador.
2. Abre el notebook en Colab y corre la primera celda de código (Paso 0): te va a pedir que subas un archivo.
3. Selecciona el CSV que descargaste. La celda lo guarda automáticamente en la carpeta `./data` (funciona tanto si el archivo se llama `Plant_health_data.csv` como `plant_health_data.csv`).

---

## ❓ Preguntas Prácticas para el Análisis

Cada ejercicio del notebook ya trae su propia pista de sintaxis/función a usar. Como guía general de lo que se evalúa en cada sesión:

* **Sesión 1:** confirma filas/columnas del dataset y que `SENSORES_NUM` coincide con las columnas reales.
* **Sesión 2:** calcula la diferencia relativa entre media y mediana para los 10 sensores. ¿Cuál tiene la mayor? Con esas cifras (todas por debajo del 1.3% en el dataset real), ¿hay evidencia de outliers fuertes, o las distribuciones son bastante simétricas?
* **Sesión 3 (dos partes):** (a) con los boxplots y el ANOVA F-test, ¿qué 2-3 sensores separan mejor las 3 clases de salud? — vas a comparar esta lista con el ranking de importancia de la Sesión 7. (b) con el promedio de `Light_Intensity` por hora de lectura, ¿hay un ciclo día/noche marcado, o no? ¿Por qué podría no haberlo en este cultivo?
* **Sesión 4:** ¿por qué `log10(x+1)` y no `log10(x)`? Identifica el sensor con mayor sesgo (`skew`) y prueba si transformarlo cambia alguna correlación de interés.
* **Sesión 5:** quita `stratify=y` de `train_test_split` y observa cuántos registros de *"High Stress"* quedan en el conjunto de prueba.
* **Sesión 6:** cambia `max_depth` del árbol CART a `2` y luego a `10`. Relaciona los cambios en F1-macro con sobreajuste (*overfitting*).
* **Sesión 7:** anota los 3 sensores con mayor importancia en tu corrida. ¿Coinciden con los que ya habías identificado en el ANOVA de la Sesión 3? Propón una explicación agronómica.
* **Sesión 8 (dos partes):** (a) CART y Random Forest llegan a 100% de accuracy — ¿eso te da confianza o sospecha? ¿Qué revisarías para descartar que el dataset se generó con umbrales simples? (b) con tus propios resultados, ¿qué modelo desplegarías en campo, considerando tanto F1-macro como el recall de *"High Stress"*?
