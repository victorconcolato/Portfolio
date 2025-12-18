import streamlit as st
import pandas as pd
import requests

st.markdown('# Ranking de nomes por década')
st.markdown('###### Confira os 20 nomes mais frequentes por década')
st.divider()

data = st.selectbox('Selecione uma década', [valor for valor in range(1930,2011,10)])

url_ranking = f'https://servicodados.ibge.gov.br/api/v2/censos/nomes/ranking/?decada={data}'
resposta_ranking = requests.get(url_ranking)

resposta_ranking = resposta_ranking.json()
#Criação do DF
df=pd.DataFrame(resposta_ranking[0]['res'],).rename(columns={'ranking':'Ranking','nome':'Nome','frequencia':'Frequência'}).set_index('Ranking')
df['Nome']=df['Nome'].str.capitalize()
df['Frequência'] = df['Frequência'].map(lambda x: f"{x:,}".replace(",", "."))
st.dataframe(df)