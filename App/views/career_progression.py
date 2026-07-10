import streamlit as st
import pandas as pd
import plotly.express as px
from collections import Counter


def show_career_progression(df):

    st.title("📈 Career Progression Dashboard")

    st.markdown("""
This dashboard shows how skill requirements change from **Fresher** to **Lead** level.
""")

    # ----------------------------
    # Experience Level Selection
    # ----------------------------

    levels = ["Fresher", "Mid", "Experienced", "Senior", "Lead"]

    available_levels = [
        level for level in levels
        if level in df["Experience_Clean"].unique()
    ]

    selected_level = st.selectbox(
        "Select Experience Level",
        available_levels
    )

    # ----------------------------
    # Filter Dataset
    # ----------------------------

    filtered_df = df[df["Experience_Clean"] == selected_level]

    # ----------------------------
    # KPI Cards
    # ----------------------------

    total_jobs = len(filtered_df)

    unique_roles = filtered_df["Title"].nunique()

    avg_skills = round(
        filtered_df["Skills_list"].apply(len).mean(),
        1
    )

    c1, c2, c3 = st.columns(3)

    c1.metric("Jobs", total_jobs)
    c2.metric("Roles", unique_roles)
    c3.metric("Avg Skills", avg_skills)

    st.divider()

    # ----------------------------
    # Top Skills
    # ----------------------------

    all_skills = sum(filtered_df["Skills_list"], [])

    skill_counts = Counter(all_skills)

    skill_df = pd.DataFrame(
        skill_counts.items(),
        columns=["Skill", "Count"]
    )

    skill_df = skill_df.sort_values(
        by="Count",
        ascending=False
    )

    st.subheader(f"🔥 Top Skills for {selected_level}")

    fig = px.bar(
        skill_df.head(10),
        x="Count",
        y="Skill",
        orientation="h",
        color="Count",
        title=f"Top Skills - {selected_level}"
    )

    fig.update_layout(
        yaxis=dict(categoryorder="total ascending")
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.divider()

    # ----------------------------
    # Top 10 Skills Table
    # ----------------------------

    st.subheader("📋 Top Skills Table")

    st.dataframe(
        skill_df.head(10),
        use_container_width=True
    )

    st.divider()

    # ----------------------------
    # Career Insight
    # ----------------------------

    st.subheader("💡 Career Insight")

    if selected_level == "Fresher":

        st.success("""
Focus on building strong fundamentals:

• Communication
• Python
• SQL
• Git
• Teamwork
""")

    elif selected_level == "Mid":

        st.info("""
Start specializing:

• Data Analysis
• Tableau
• Power BI
• SQL
• Python
""")

    elif selected_level == "Experienced":

        st.warning("""
Industry expects advanced technical skills:

• AWS
• Docker
• Kubernetes
• Leadership
• CI/CD
""")

    elif selected_level == "Senior":

        st.success("""
Senior professionals require:

• Spark
• Hadoop
• Snowflake
• Python
• Power BI
""")

    elif selected_level == "Lead":

        st.error("""
Leadership skills dominate:

• Mentoring
• Strategic Planning
• Team Management
• Project Leadership
""")