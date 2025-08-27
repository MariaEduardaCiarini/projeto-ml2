import yfinance as yf
import streamlit as st


def app():
    st.write("""
    # Aplicativo de Preços Históricos de FIIs

    Este aplicativo exibe os preços de **Abertura e Fechamento** do FII selecionado para o ano de 2025.
    """)

    # Opções de FIIs
    tickers = {
        "KNCR11": "KNCR11.SA",
        "RECR11": "RECR11.SA",
        "KNHY11": "KNHY11.SA"
    }

    # Selectbox na barra lateral
    fii_escolhido = st.sidebar.selectbox(
        "Selecione o FII:", list(tickers.keys()))

    # Obter dados do FII escolhido (somente 2025)
    ticker_symbol = tickers[fii_escolhido]
    ticker_data = yf.Ticker(ticker_symbol)
    ticker_df = ticker_data.history(start="2025-01-01", end="2025-12-31")

    st.subheader(f'📈 {fii_escolhido} - Preço de Abertura (2025)')
    st.line_chart(ticker_df['Open'])

    st.subheader(f'📉 {fii_escolhido} - Preço de Fechamento (2025)')
    st.line_chart(ticker_df['Close'])
