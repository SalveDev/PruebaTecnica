# Prueba Técnica — Alertas de Stock

Gracias por participar en nuestro proceso.  
Este ejercicio está diseñado para evaluar tu capacidad de razonamiento, transformación de datos y presentación de resultados utilizando Python y Pandas.

No buscamos perfección: buscamos claridad, criterio y una solución funcional.

---

## ⏱️ Tiempo estimado

Este ejercicio está pensado para resolverse en **aproximadamente 2 horas**.  
No es necesario terminar todo para continuar con el proceso; si el tiempo se termina, entrega lo que tengas.

---

## 🎯 Objetivo

Construir una página en Flask que muestre una tabla de **productos en riesgo de agotamiento**, calculados a partir de datos en formato Parquet.

Debes completar la lógica necesaria dentro del endpoint:

```
/alertas
```

y renderizar el resultado en el archivo:

```
templates/alertas.html
```

El archivo HTML ya está preparado para recibir la lista `alertas`.

---

## 📂 Archivos proporcionados

La carpeta contiene:

```
app/
  app.py
  data/
    articulos.parquet
    stock.parquet
    ventas.parquet
    sucursales.parquet
  templates/
    alertas.html
  static/
    js/
    css/
      alertas.css
  requirements.txt
  README.md
```

---

## 🧠 Tareas a realizar

Completa la función del endpoint `/alertas` para:

### 1. Cargar los archivos Parquet de la carpeta `data/`

### 2. Calcular la rotación diaria promedio por sucursal y artículo  

Usa **solo** las ventas del mes de Octubre.

Fórmula sugerida:

```
rotacion = total_vendido_30_dias / 30
```

### 3. Combinar los datos de rotación con el stock actual

### 4. Calcular los días de inventario (DOI)

```
DOI = stock / rotacion
```

### 5. Identificar productos en riesgo  
Filtrar donde:

- rotación > 0  
- DOI <= 7 días  

### 6. Ordenar la tabla resultante por:

- DOI ascendente  
- Rotación descendente

### 7. Renderizar la tabla usando `alertas.html`  
Convierte el DataFrame a:

```
alertas = df.to_dict(orient="records")
```

y pásalo al template.

---

## 🌐 Resultado esperado

Una tabla HTML mostrando:

| Sucursal | Nombre Sucursal | Artículo | Descripción | Rotación | Stock | DOI 

No se exige:

- CSS avanzado  
- Semáforos  
- Visualizaciones  
- Recomendaciones  
- Manejo sofisticado de errores  

Si alcanzas a agregar extras, son bienvenidos.

---

## 🚀 Ejecutar el proyecto

1. Instala dependencias:

```
pip install -r requirements.txt
```

2. Ejecuta la app:

```
python app.py
```

3. Visita:

```
http://localhost:80/alertas
```

---

## 📝 Entrega

Puedes entregar:

- El código final (modificado en `app.py`)  
- Cualquier nota adicional necesaria  

---

## 💡 Notas importantes

- No necesitas crear nuevos endpoints.  
- No se evalúa estilo visual, sino razonamiento y funcionalidad.  
- Si no terminas todo dentro del tiempo, entrega lo que tengas implementado.

---

## 🤝 Gracias

Apreciamos mucho tu tiempo.  
Si en cualquier momento te sientes bloqueado, puedes avisarnos durante la entrevista.

¡Éxito en el ejercicio! 🚀
