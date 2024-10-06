import pandas as pd
import plotly.express as px
import streamlit as st

df_autos = pd.read_csv('vehicles_us.csv')
boton_histograma = st.button('Construir Histograma')

if boton_histograma:
    st.write('Creamos un histograr para anuncios de coches')
    fig = px.histogram(df_autos, x='odometer')
    st.plotly_chart(fig, use_container_width=True)
