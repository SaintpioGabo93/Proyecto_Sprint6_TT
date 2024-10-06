#Importamos las librerias
import pandas as pd
import plotly.express as px
import streamlit as st

# Creamos las variables para los objetos
df_autos = pd.read_csv("vehicles_us.csv")
boton_histograma = st.button("Construir Histograma")
boton_dispersion = st.button("Construir Grafico de Dispersion")
casilla_histograma = st.checkbox("Construir casilla de verificacion histograma")
casilla_dispersion = st.checkbox("Construir casilla de verificacion grafico de dispersion")

# Creamos el boton de histograma
if boton_histograma:
    st.write("Creamos un histograma para anuncios de coches")
    fig = px.histogram(df_autos, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

#Creamo el boton de grafico de dispesion
if boton_dispersion:
    st.write("Creamos un grafico de dispersion para anuncios de coches")
    fig = px.scatter(df_autos, x="odometer", y="price")
    st.plotly_chart(fig, use_container_width=True)

# Creamos el boton de verificacion histograma 
if casilla_histograma:
    st.write("Construccion de un histograma para la columna odometro con boton de verificacion")
    fig = px.histogram(df_autos, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

# Creamos el boton de verificacion grafico de dispersion
if casilla_dispersion:
    st.write("Construccion de un histograma para la columna odometro con boton de verificacion")
    fig = px.scatter(df_autos, x="odometer", y="price")
    st.plotly_chart(fig, use_container_width=True)
