import streamlit as st
import requests
from pprint import pprint
import pandas as pd

st.markdown('# Comparação entre nomes')
st.divider()
#Criação das colunas 
col00, col10 = st.columns(2)
#Gravação dos dados na sessão com tratamento de acentos e colocando todos em letra maiuscula
st.session_state['nome_0'] = col00.text_input('Digite o primeiro nome',key=0).upper().replace("Ã","A").replace("Á","A").replace("É","E").replace("Í","I").replace("Ó","O").replace("Ú","U").replace("Ç","C").upper()
st.session_state['nome_1'] = col10.text_input('Digite o segundo nome',key=1).upper().replace("Ã","A").replace("Á","A").replace("É","E").replace("Í","I").replace("Ó","O").replace("Ú","U").replace("Ç","C").upper()

#Criação de variável para as chaves gravadas na sesão
nome_0 = st.session_state['nome_0']
nome_1 = st.session_state['nome_1']
enviar = st.button('Enviar')


st.divider()
try:
    #Caso aperte o botao enviar e os dois nomes estejam vazios, FAÇA:
    if enviar and nome_0!="" and nome_1!="":
    #Cacheamento de dados para solicitar os dados somente uma vez
        @st.cache_data
        def requisicao_ibge(nome_0,nome_1):
            url = f"https://servicodados.ibge.gov.br/api/v2/censos/nomes/{nome_0}|{nome_1}"
            resposta = requests.get(url)
            return resposta.json()
        #Gravação da execução dos dados na variavel resposta
        resposta = requisicao_ibge(nome_0,nome_1)
        
        dicionario_referencia = {resposta[0]['nome']:resposta[0]['res'],
                                 resposta[1]['nome']:resposta[1]['res']
                                 }
        
#Se resposta não for vazio, FAÇA:
        if resposta:
            dicionario_full = pd.DataFrame({
                'Período':[x['periodo'] for x in dicionario_referencia[nome_0]],
                
                f'Frequência | {nome_0.capitalize()}':[x['frequencia'] for x in dicionario_referencia[nome_0]],
                
                f'Frequência | {nome_1.capitalize()}':[x['frequencia'] for x in dicionario_referencia[nome_1]]
                })
            
            dicionario_full['Nome mais popular'] = dicionario_full.apply(lambda row: nome_0.capitalize() if row[f'Frequência | {nome_0.capitalize()}'] > row[f'Frequência | {nome_1.capitalize()}'] else nome_1.capitalize(), axis=1 )
            dicionario_full['Período'] = dicionario_full['Período'].str.replace("[","")
            dicionario_full.set_index('Período',inplace=True)
            
#Widget de FREQUÊNCIA TOTAL
            col01, col11 = st.columns(2)
            
            col01.markdown(f'#### Frequência Total | {nome_0.capitalize()}')
            
            col01.markdown(f'### {dicionario_full[f'Frequência | {nome_0.capitalize()}'].sum():,}'.replace(",", "."))

            col11.markdown(f'#### Frequência Total | {nome_1.capitalize()}')
            col11.markdown(f'### {int(dicionario_full[f'Frequência | {nome_1.capitalize()}'].sum()):,}'.replace(",", "."))
            st.divider()

# Qual nome foi mais popular em cada período.
            df = pd.DataFrame(dicionario_full)
            st.dataframe(df)
            
    if enviar and nome_0!="" or nome_1!="":
        st.warning('Preencha os dois campos com nomes')
    
        
except requests.exceptions.JSONDecodeError:
    pass
except IndexError:
    st.error('Um dos nomes não foi encontrado na base do IBGE.')
