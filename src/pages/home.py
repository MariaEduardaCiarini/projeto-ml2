import streamlit as st


def app():
    st.set_page_config(page_title="Home", page_icon="🏠", layout="centered")

    st.markdown(
        """
        <div style="text-align: center;">
            <h1 style="color:Green;">🏠 Bem-vindo ao Aplicativo</h1>
            <h3 style="color:blue;">Sua central de navegação</h3>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.divider()

    # Mensagem inicial
    st.markdown(
        """
        ### 👋 Bem Vindo(a)!
        Esta é a página **inicial** do aplicativo.

        ➡️ Use a **barra lateral** para navegar entre as páginas disponíveis.  
        🚀 Explore os recursos e aproveite a experiência!
        """
    )
    st.divider()

    st.success("✅ Você está na página inicial!")
