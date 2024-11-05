import streamlit as st
import pandas as pd
import plotly.express as px

car_df= pd.read_csv('vehicles_us.csv')
st.header('Proyecto del Sprint 6')
hist_button= st.button('Crear Histograma')
hist_button= st.button('Crear Gráfico de Dispersión')

if hist_button:
    st.write('Creación de un histograma de anuncios de ventas de autos en EUA')

fig = px.histogram(car_df, x= 'odometer')
st.plotly_chart(fig, use_container_width=True)

##Sustituir los botones por casillas de verificación en streamlit
#st.checkbox()


