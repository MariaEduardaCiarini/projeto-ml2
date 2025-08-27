import streamlit as st
from src.pages.home import app as home
from src.pages.analytics import app as analytics

st.set_page_config(page_title="Meu App", page_icon="📊", layout="wide")

st.markdown(
    """
    <style>
    [data-testid="stSidebar"] {
        background-color: #1E1E2F;
        padding: 20px;
    }
    [data-testid="stSidebar"] h2 {
        color: #4CAF50;
        text-align: center;
        margin-bottom: 20px;
    }
    .menu-item {
        font-size: 18px;
        padding: 10px;
        border-radius: 8px;
        margin-bottom: 5px;
        cursor: pointer;
    }
    .menu-item:hover {
        background-color: #33334d;
    }
    .selected {
        background-color: #4CAF50 !important;
        color: white !important;
        font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --- Sidebar ---
st.sidebar.title("🚀 Navegação")

# Ícones + páginas
menu = {
    "🏠 Home": "home",
    "📈 Analytics": "analytics",
}

escolha = st.sidebar.radio("Escolha a página:", list(menu.keys()))

# --- Controle das páginas ---
if menu[escolha] == "home":
    home()
elif menu[escolha] == "analytics":
    analytics()
