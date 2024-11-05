import streamlit as st
import pandas as pd
import plotly.express as px

car_df= pd.read_csv('vehicles_us.csv')
st.header('Proyecto del Sprint 6')
hist_button= st.button('Crear Histograma')
disp_button= st.button('Crear Gráfico de Dispersión')
hist_pg_button= st.checkbox('Crear Histograma en una página nueva')
disp_pg_button= st.checkbox('Crear Gráfico de Dispersión en una página nueva')


if hist_button:
    st.write('Creación de un histograma de anuncios de ventas de autos en EUA')
    fig = px.histogram(car_df, x= 'odometer')
    st.plotly_chart(fig, use_container_width=True)

if disp_button:
    st.write('Creación de un gráfico de dispersión de anuncios de ventas de autos en EUA')
    fig = px.scatter(car_df, x="odometer", y="price") 
    st.plotly_chart(fig, use_container_width=True)

if disp_pg_button:
    st.write('Redirigiendo...')
    fig1 = px.scatter(car_df, x="odometer", y="price")
    fig1.show() # crear gráfico de dispersión

if hist_pg_button:
    st.write('Redirigiendo...')
    fig2 = px.histogram(car_df, x="odometer") 
    fig2.show() 


##Sustituir los botones por casillas de verificación en streamlit
#st.checkbox()


