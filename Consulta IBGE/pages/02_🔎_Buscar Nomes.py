import streamlit as st
import requests
from pprint import pprint
import pandas as pd

st.markdown('# Busca de nomes')
st.divider()


try:
#Usuário digita o nome a ser pesquisado
    nome = st.text_input('Digite um Nome: ')
    
#Busca na API pelo nome
    url = f'https://servicodados.ibge.gov.br/api/v2/censos/nomes/{nome}'
    resposta = requests.get(url)
    resposta = resposta.json().copy()

#Caso o nome seja diferente de vazio, faça:
    if nome != "" and resposta:
#Ajuste o nome para retirar espaços e colocar a letra em maiúscula
        nome_up = nome.upper()
#Layout personalizado
        st.markdown(f'#### Nome selecionado: {nome}')
# Frequência total desse nome no Brasil.
#Para cada item na lista 'resposta[0]['res']', pegue o todos os valores da key 'item['frequencia']' e some. 
        total_freq = sum(item['frequencia'] for item in resposta[0]['res'])

        st.write(f'O total de vezes que o nome {nome} foi cadastrado é de {total_freq:,} vezes.'.replace(",", "."))
                
        st.divider()

#Distribuição por década (tabela).
#Criação e ajuste do DF.
        df_frequencia_nome = pd.DataFrame(resposta[0]['res'])
        
        df_frequencia_nome['periodo'] = df_frequencia_nome['periodo'].str.replace("[","", regex=False).str.replace(","," - ", regex=False)
        df_frequencia_nome = df_frequencia_nome.rename(columns={'periodo':'Período','frequencia':'Frequência'})
        df_frequencia_nome.set_index('Período', inplace=True)
#Exibição do DF
        df_frequencia_nome['Frequência'] = df_frequencia_nome['Frequência'].map(lambda x: f"{x:,}".replace(",", "."))
        st.dataframe(df_frequencia_nome)
        
#Década de maior popularidade com um insight em texto.
        ano_popularidade = df_frequencia_nome['Frequência'].idxmax()
        
        st.markdown(f"#### O período de maior popularidade do nome ' {nome} ' ocorreu entre {ano_popularidade.replace('-','e')}")
    elif not resposta:
        st.error('Nome não encontrado na base de dados do IBGE. Tente novamente')
except requests.exceptions.JSONDecodeError:
    pass