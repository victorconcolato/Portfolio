import streamlit as st

st.markdown('### Bem vindo!')
st.markdown('### Neste app, você poderá verifica o histórico de utilização de qualquer nome, usando a base do IBGE')
st.markdown('### Período considerado: 1930 a 2010, por década.')
st.markdown('### Considerações importantes:')

st.markdown('##### → O Censo Demográfico 2010 não considerou nos questionários nomes compostos. Por esta razão, este programa não retorna resultados ao consultar nomes compostos.')
            
st.markdown('##### → A API não considera o uso de sinais diacríticos(acentos, cedilha, trema e til), de forma que Antônio e Antonio são contabilizados como Antonio.')


col01, col02, col03= st.columns(3)


col01.markdown(
    """
<a href="https://github.com/victorconcolato">
<img src="https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png" width="25">
</a>""",
unsafe_allow_html=True
)

col02.markdown(
    """
    <a href="https://wa.me/5521983811828">
        <img src="https://upload.wikimedia.org/wikipedia/commons/6/6b/WhatsApp.svg" width="25">
    </a>
    """,
    unsafe_allow_html=True
)

col03.markdown(
    """
<a href="https://www.instagram.com/victor.vianac/">
<img src="https://upload.wikimedia.org/wikipedia/commons/a/a5/Instagram_icon.png" width="25">
</a>""",
unsafe_allow_html=True
)







# col01.markdown(f'(st.image("https://upload.wikimedia.org/wikipedia/commons/6/6b/WhatsApp.svg", width=25))[https://wa.me/5521983811828]')


# col02.image("https://upload.wikimedia.org/wikipedia/commons/a/a5/Instagram_icon.png", width=25)
# col03.image("https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png", width=25)

