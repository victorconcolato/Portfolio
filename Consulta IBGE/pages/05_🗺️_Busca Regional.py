import streamlit as st
import requests
import pandas as pd

st.markdown('# Busca Regional')
st.divider()

#Criação de dicionário para identificação dos estados.
url_estado = 'https://servicodados.ibge.gov.br/api/v1/localidades/estados'
resposta_estado = requests.get(url_estado)
resposta_estado = resposta_estado.json().copy()
nome_estados = [item['nome'] for item in resposta_estado]
id_estados = [item['id'] for item in resposta_estado]
dict_estados = dict(zip(nome_estados,id_estados))

#Criação do Streamlit.
nome = st.text_input('Informe o Nome')
id_estado=st.selectbox('Selecione o Estado',dict_estados.keys())
try:
    
    if nome and id_estado != "":
        url_nome =f'https://servicodados.ibge.gov.br/api/v2/censos/nomes/{nome}?localidade={id_estado}'
        resposta = requests.get(url_nome)
        resposta = resposta.json().copy()

        df_local = pd.DataFrame(resposta[0]['res']).rename(columns={'periodo':'Período','frequencia':'Frequência'})
        df_local['Período']=df_local['Período'].str.replace("[","").str.replace(',',' - ')
        df_local.set_index('Período', inplace=True)
        df_local['Frequência'] = df_local['Frequência'].map(lambda x: f"{x:,}".replace(",", "."))
        st.dataframe(df_local)

except requests.exceptions.JSONDecodeError:
    pass



