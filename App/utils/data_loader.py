import pandas as pd
import streamlit as st


@st.cache_data
def load_data():
    """
    Load and preprocess the dataset
    """

    df = pd.read_csv("../Data/cleaned_jobs.csv")

    # Convert Skills column into list
    df["Skills_list"] = df["Skills"].apply(
        lambda x: [skill.strip() for skill in str(x).split(";")]
    )

    return df