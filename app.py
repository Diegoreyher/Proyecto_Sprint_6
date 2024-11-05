import streamlit as st
import pandas as pd
import plotly.express as px

car_df= pd.read_csv('vehicles_us.csv')
st.header('Proyecto del Sprint 6')
hist_button= st.button('Crear Histograma')
disp_button= st.button('Crear Gráfico de Dispersión')
hist_pg_button= st.checkbox('Crear Histograma en color verde')
disp_pg_button= st.checkbox('Crear Gráfico de Dispersión en color verde')


if hist_button:
    st.write('Creación de un histograma de anuncios de ventas de autos en EUA')
    fig = px.histogram(car_df, x= 'odometer')
    st.plotly_chart(fig, use_container_width=True)

if disp_button:
    st.write('Creación de un gráfico de dispersión de anuncios de ventas de autos en EUA')
    fig = px.scatter(car_df, x="odometer", y="price") 
    st.plotly_chart(fig, use_container_width=True)

if disp_pg_button:
    st.write('Creación de un gráfico de dispersión de anuncios de ventas de autos en EUA')
    fig = px.scatter(car_df, x="odometer", y="price", color_discrete_sequence=["green"])
    st.plotly_chart(fig, use_container_width=False)

if hist_pg_button:
    st.write('Creación de un histograma de anuncios de ventas de autos en EUA')
    fig = px.histogram(car_df, x="odometer", color_discrete_sequence=["green"])
    st.plotly_chart(fig, use_container_width=False)

##Sustituir los botones por casillas de verificación en streamlit
#st.checkbox()


