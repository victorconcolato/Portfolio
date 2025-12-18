import streamlit as st

st.markdown('# Bem vindo!')
st.markdown('# Neste app, você poderá verifica o histórico de utilização de qualquer nome, usando a base do IBGE')
st.markdown('# O período vai de 1930 a 2010, por década.')
st.markdown('# Perguntas Frequentes:')
st.markdown("""####
            Quando consulto nomes compostos, por exemplo, Maria dos Anjos, Maria Luiza etc, a API não retorna nenhum resultado. Por quê ?      
                → O Censo Demográfico 2010 não considerou nos questionários nomes compostos, apenas o primeiro nome e o último sobrenome. Por essa razão, esta API não retorna resultados ao consultar nomes compostos.
            
            A API distingue nomes diferenciados somente pelo uso de sinais diacríticos (acento agudo, acento circunflexo, acento grave, cedilha, trema e til) como, por exemplo, Antônio e Antonio ?

                → A API não considera o uso de sinais diacríticos, de forma que Antônio e Antonio são contabilizados como Antonio. 
            """)

st.markdown('###### Produzido por (Victor Viana Concolato)[https://github.com/victorconcolato]')