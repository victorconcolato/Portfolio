import streamlit as st
import requests
from pprint import pprint

nome = 'joao'
url = f'https://servicodados.ibge.gov.br/api/v2/censos/nomes/{nome}'

resposta = requests.get(url).json()
pprint(resposta)
pprint(resposta[0]['res'][1]['frequencia'])

