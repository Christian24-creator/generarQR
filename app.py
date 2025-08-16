import streamlit as st
import pandas as pd
import numpy as np

# Título de la aplicación
st.title('Mi primera aplicación de Streamlit')

# Un encabezado
st.header('Análisis de datos')

# Un texto simple
st.write('¡Hola, mundo! Aquí puedes visualizar tus datos de manera interactiva.')

# Crear datos de ejemplo
data = pd.DataFrame({
    'columna_1': [1, 2, 3, 4],
    'columna_2': [10, 20, 30, 40]
})

# Mostrar los datos en una tabla
st.subheader('Datos de ejemplo')
st.dataframe(data)

# Crear un gráfico de líneas
st.subheader('Gráfico de ejemplo')
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c']
)
st.line_chart(chart_data)

# Añadir un control interactivo (slider)
st.subheader('Slider interactivo')
x = st.slider('Selecciona un valor para x', min_value=0, max_value=100)
st.write('El valor de x es:', x)