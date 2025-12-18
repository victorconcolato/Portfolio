import streamlit as st
import requests
from pprint import pprint
import pandas as pd

st.markdown('# Comparação entre nomes')
st.divider()
col00, col10 = st.columns(2)

st.session_state['nome_0'] = col00.text_input('Digite o primeiro nome',key=0).upper().replace("Ã","A").replace("Á","A").replace("É","E").replace("Í","I").replace("Ó","O").replace("Ú","U").replace("Ç","C")
st.session_state['nome_1'] = col10.text_input('Digite o segundo nome',key=1).upper().replace("Ã","A").replace("Á","A").replace("É","E").replace("Í","I").replace("Ó","O").replace("Ú","U").replace("Ç","C")

nome_0 = st.session_state['nome_0']
nome_1 = st.session_state['nome_1']
enviar = st.button('Enviar')
st.divider()
try:
    @st.cache_data
    def requisicao_ibge():
        url = f"https://servicodados.ibge.gov.br/api/v2/censos/nomes/{nome_0}|{nome_1}"
        resposta = requests.get(url)
        return resposta.json()
    
    resposta = requisicao_ibge()

    if enviar and nome_0!="" and nome_1!="":
        
#Se resposta não for vazio, FAÇA:
        if resposta:
            
#Se o primeiro valor da lista tiver com o nome igual ao enviado pelo usuário, FAÇA:
#Este if/else, evita o problema da API enviar os dados trocados.
#Caso o valor coincida com o JSON enviado pela API, faça:

            if nome_0 == resposta[0]['nome']:
                tot_freq_nome_0 = sum(item['frequencia'] for item in resposta[0]['res']) 
                tot_freq_nome_1 = sum(item['frequencia'] for item in resposta[1]['res'])

#Caso a API envie os dados contrários(nome_01 como segundo item da lista), FAÇA:
#Esta forma é possível pois só há 2 valores.
            else:
                tot_freq_nome_0 = sum(item['frequencia'] for item in resposta[1]['res'])
                tot_freq_nome_1 = sum(item['frequencia'] for item in resposta[0]['res'])
            
            
            col01, col11 = st.columns(2)
            
            col01.markdown(f'#### Frequência Total | {nome_0.capitalize()}')
            col01.markdown(f'### {tot_freq_nome_0:,}'.replace(",", "."))

            col11.markdown(f'#### Frequência Total | {nome_1.capitalize()}')
            col11.markdown(f'### {tot_freq_nome_1:,}'.replace(",", "."))
            st.divider()

#Criação dos DF para facilitar a tabela(Poderia ser mais pythônico.).

            df0=pd.DataFrame(resposta[0]['res'])
            df0=df0.rename(columns={'periodo':'Período', 'frequencia': 'Frequência'})
            df0['Período']=df0['Período'].str.replace('[',"" and ',').str.replace(',',' - ')
            df0.set_index('Período', inplace=True)

            df1=pd.DataFrame(resposta[1]['res'])
            df1=df1.rename(columns={'periodo':'Período', 'frequencia': 'Frequência'})
            df1['Período']=df1['Período'].str.replace('[',"" and ',').str.replace(',',' - ')
            df1.set_index('Período', inplace=True)
# Qual nome foi mais popular em cada período.
            df_03 = pd.DataFrame({f'Frequência {nome_0}':df0['Frequência'],f'Frequência {nome_1}':df1['Frequência']})
            
#Criar a coluna 'Nome mais popular' usando o df_03.
#Aplique no df_03, para cada linha da coluna 'Nome mais popular', conforme o caso:
#nome_0 SE a linha 

            df_03['Nome mais popular'] = df_03.apply(lambda row : nome_0.capitalize() if row[f'Frequência {nome_0}']> row [f'Frequência {nome_1}'] else nome_1.capitalize(), axis=1)
            st.markdown("## Nome mais popular por período")
            
            df_03[f'Frequência {nome_0}'] = df_03[f'Frequência {nome_0}'].map(lambda x: f"{x:,}".replace(",", "."))
            df_03[f'Frequência {nome_1}'] = df_03[f'Frequência {nome_1}'].map(lambda x: f"{x:,}".replace(",", "."))
            st.dataframe(df_03)
except requests.exceptions.JSONDecodeError:
    pass

