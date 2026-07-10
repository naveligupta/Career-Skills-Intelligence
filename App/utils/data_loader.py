from pathlib import Path
import pandas as pd
import streamlit as st


@st.cache_data
def load_data():
    """
    Load and preprocess the jobs dataset.
    """

    # Project root folder
    BASE_DIR = Path(__file__).resolve().parents[2]

    # Dataset path
    DATA_PATH = BASE_DIR / "Data" / "cleaned_jobs.csv"

    # Read CSV
    df = pd.read_csv(DATA_PATH)

    # Convert Skills column into list
    if "Skills" in df.columns:
        df["Skills_list"] = df["Skills"].fillna("").apply(
            lambda x: [skill.strip() for skill in str(x).split(";") if skill.strip()]
        )

    # Clean Experience column (if present)
    if "Experience" in df.columns:
        df["Experience_Clean"] = (
            df["Experience"]
            .astype(str)
            .str.strip()
        )

    return df