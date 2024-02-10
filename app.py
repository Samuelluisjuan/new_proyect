import pandas as pd
import plotly.express as px
import streamlit as st
        
car_data = pd.read_csv('vehicles_us.csv')  # Leer los datos

# Crear un título para la aplicación
st.title('Análisis de vehículos vendidos')

show_hist = st.checkbox('Mostrar histograma') # Casillas de verificación para visualizaciones
show_scatter = st.checkbox('Mostrar scatterplot') # Casillas de verificación para visualizaciones

# Si se selecciona la casilla de verificación para el histograma
if show_hist:
    # Crear un título para el histograma
    st.header('Histograma de odómetros')
    
    # Crear un histograma
    fig_hist = px.histogram(car_data, x="odometer")
    
    # Mostrar el histograma
    st.plotly_chart(fig_hist, use_container_width=True)

# Si se selecciona la casilla de verificación para el scatterplot
if show_scatter:
    # Crear un título para el scatterplot
    st.header('Gráfico de dispersión entre año de fabricación y precio')
    
    # Crear el scatterplot
    fig_scatter = px.scatter(car_data, x="year", y="price", 
                             title="Precio vs. Año de Fabricación",
                             labels={"year": "Año de Fabricación", "price": "Precio"})
    
    # Mostrar el scatterplot
    st.plotly_chart(fig_scatter, use_container_width=True)