import streamlit as st

from utils.data_loader import load_data
from views.home import show_home
from views.market_analysis import show_market_analysis
from views.career_progression import show_career_progression
#from views.skill_gap import show_skill_gap
from views.about import show_about
# ----------------------------
# Page Configuration
# ----------------------------

st.set_page_config(
    page_title="Career Skills Intelligence",
    page_icon="🎯",
    layout="wide"
)

# ----------------------------
# Load Data
# ----------------------------

df = load_data()

# ----------------------------
# Sidebar
# ----------------------------

st.sidebar.title("🎯 Navigation")

page = st.sidebar.radio(
    "Go To",
    [
        "🏠 Home",
        "📊 Market Analysis",
        "📈 Career Progression",
        "ℹ️ About"
    ]
)

# ----------------------------
# Navigation
# ----------------------------

if page == "🏠 Home":
    show_home(df)

elif page == "📊 Market Analysis":
    show_market_analysis(df)

elif page == "📈 Career Progression":
    show_career_progression(df)

elif page == "ℹ️ About":
    show_about()