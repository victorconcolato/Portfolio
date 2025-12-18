import streamlit as st
import requests
from pprint import pprint
import pandas as pd

st.markdown('# Evolução dos nomes')
st.markdown('###### Veja em gráficos a utilização dos nomes ao longo do tempo')
st.divider()


try:
#Usuário digita o nome a ser pesquisado
    nome = st.text_input('Digite um Nome: ')

#Busca na API pelo nome
    url = f'https://servicodados.ibge.gov.br/api/v2/censos/nomes/{nome}'
    resposta = requests.get(url)
    resposta = resposta.json().copy()

    df = pd.DataFrame(resposta[0]['res']).rename(columns={'periodo':'Período','frequencia':'Frequência'})
    df['Período']=df['Período'].str.replace("[","").str.replace(',',' - ')
    df.set_index('Período',inplace=True)
    df['Frequência'] = df['Frequência'].map(lambda x: f"{x:,}".replace(",", "."))
    st.line_chart(df['Frequência'])
    st.dataframe(df)
except requests.exceptions.JSONDecodeError:
    pass