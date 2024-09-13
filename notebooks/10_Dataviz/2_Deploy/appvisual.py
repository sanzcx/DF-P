import plotly.express as px
df = px.data.gapminder()
import plotly.express as px
import streamlit as st
df = px.data.gapminder()
continente = df['continent'].unique()
continente = st.selectbox(label='Seleccione continente', options=continente)
mask = df['continent'] == continente
dff = df[mask]
fig = px.line(data_frame=dff, x='year', y='lifeExp')
st.plotly_chart(fig)

