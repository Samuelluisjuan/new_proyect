import pandas as pd
import plotly.express as px
import streamlit as st
        
try:
    car_data = pd.read_csv('vehicles_us.csv') # leer los datos
    
    hist_button = st.button('Construir histograma') # crear un botón
        
    if hist_button: # al hacer clic en el botón
        # escribir un mensaje
        st.write('Histograma del odómetro para el conjunto de datos de anuncios de venta de coches')
                
        # crear un histograma
        fig = px.histogram(car_data, x="odometer")
        
        # añadir título y etiquetas
        fig.update_layout(
            title="Distribución del odómetro",
            xaxis_title="Odómetro",
            yaxis_title="Frecuencia"
        )
        
        # mostrar un gráfico Plotly interactivo
        st.plotly_chart(fig, use_container_width=True)
