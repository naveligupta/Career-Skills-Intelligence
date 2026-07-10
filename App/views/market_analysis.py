import streamlit as st
import pandas as pd
import plotly.express as px
from collections import Counter


def show_market_analysis(df):

    st.title("📊 Market Analysis Dashboard")

    st.write("Explore job market trends and skill demand.")

    # -----------------------
    # KPI Cards
    # -----------------------

    total_jobs = len(df)
    unique_roles = df["Title"].nunique()
    experience_levels = df["Experience_Clean"].nunique()
    avg_skills = round(df["Skills_list"].apply(len).mean(), 1)

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("📄 Jobs", total_jobs)
    c2.metric("💼 Roles", unique_roles)
    c3.metric("📈 Experience", experience_levels)
    c4.metric("🛠 Avg Skills", avg_skills)

    st.divider()

    # -----------------------
    # Top Skills
    # -----------------------

    st.subheader("🔥 Top 20 Most In-Demand Skills")

    all_skills = sum(df["Skills_list"], [])

    skill_counts = Counter(all_skills)

    skill_df = pd.DataFrame(
        skill_counts.items(),
        columns=["Skill", "Count"]
    )

    skill_df = skill_df.sort_values(
        by="Count",
        ascending=False
    )

    fig = px.bar(
        skill_df.head(20),
        x="Count",
        y="Skill",
        orientation="h",
        color="Count",
        title="Top Skills Across All Jobs"
    )

    fig.update_layout(
        yaxis=dict(categoryorder="total ascending")
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.divider()

    # -----------------------
    # Experience Distribution
    # -----------------------

    st.subheader("📈 Experience Level Distribution")

    exp_df = (
        df["Experience_Clean"]
        .value_counts()
        .reset_index()
    )

    exp_df.columns = ["Experience", "Count"]

    fig2 = px.pie(
        exp_df,
        names="Experience",
        values="Count",
        hole=0.4,
        title="Experience Distribution"
    )

    st.plotly_chart(
        fig2,
        use_container_width=True
    )