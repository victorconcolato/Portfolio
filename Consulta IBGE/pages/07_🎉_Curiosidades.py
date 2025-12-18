import streamlit as st
import requests
from pprint import pprint
import pandas as pd

st.markdown('# Curiosidades sobre os nomes')
st.markdown('###### Descubra os nomes destaques de 1930 - 2010')
st.divider()


try:
    st.markdown('### Nome mais popular de todos')
#Busca na API pelo nome
    url = f'https://servicodados.ibge.gov.br/api/v2/censos/nomes/ranking/'
    resposta = requests.get(url)
    resposta = resposta.json().copy()
    
    df_ranking = pd.DataFrame(resposta[0]['res']).rename(columns={'nome':'Nome','frequencia':'Frequência','ranking':'Ranking'}).set_index('Ranking')
    df_ranking['Nome']=df_ranking['Nome'].str.capitalize()
    df_ranking['Frequência']=df_ranking[f'Frequência'].map(lambda x: f"{x:,}".replace(",", "."))
    
    
    st.markdown('### Ranking Absoluto')    
    st.dataframe(df_ranking)
    
    st.markdown('### Nome mais popular de todos')
    st.write(f'O nome mais popular de todos é {resposta[0]['res'][0]['nome'].capitalize()} com {resposta[0]['res'][0]['frequencia']:,} votos!'.replace(",","."))
    st.markdown('### Confira o gráfico abaixo!')
    df_grafico=df_ranking.set_index('Nome')
    df_grafico['Frequência']=df_grafico['Frequência'].str.replace(".","").map(lambda x: int(x))
    st.bar_chart(df_grafico)
except requests.exceptions.JSONDecodeError:
    pass