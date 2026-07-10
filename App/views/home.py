import streamlit as st


def show_home(df):

    # -----------------------------
    # Title
    # -----------------------------

    st.title("🎯 Career Skills Intelligence Platform")

    st.markdown("""
### Analyze • Compare • Upskill

A data-driven platform that helps students and job seekers understand the current job market,
identify in-demand skills, analyze career progression, and discover their skill gaps.
""")

    st.divider()

    # -----------------------------
    # KPI Cards
    # -----------------------------

    total_jobs = len(df)
    total_roles = df["Title"].nunique()
    total_levels = df["Experience_Clean"].nunique()

    avg_skills = round(
        df["Skills_list"].apply(len).mean(),
        1
    )

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "📄 Total Jobs",
            total_jobs
        )

    with col2:
        st.metric(
            "💼 Job Roles",
            total_roles
        )

    with col3:
        st.metric(
            "📈 Experience Levels",
            total_levels
        )

    with col4:
        st.metric(
            "🛠 Avg Skills / Job",
            avg_skills
        )

    st.divider()

    # -----------------------------
    # Features
    # -----------------------------

    st.subheader("✨ What Can This Platform Do?")

    col1, col2 = st.columns(2)

    with col1:

        st.success("📊 Market Analysis")

        st.write(
            "• Explore in-demand skills\n"
            "• Analyze job market trends\n"
            "• Discover popular job roles"
        )

        st.success("📈 Career Progression")

        st.write(
            "• Compare skills across experience levels\n"
            "• Understand career growth\n"
            "• Discover emerging technologies"
        )

    with col2:

        st.success("🎯 Skill Gap Analyzer")

        st.write(
            "• Compare your skills with job requirements\n"
            "• View your match score\n"
            "• Identify missing skills"
        )

        st.success("📚 Personalized Roadmap")

        st.write(
            "• Get learning recommendations\n"
            "• Understand what to learn next\n"
            "• Become placement ready"
        )

    st.divider()

    # -----------------------------
    # Dataset Overview
    # -----------------------------

    st.subheader("📂 Dataset Overview")

    st.write(
        "The dashboard is built using a curated dataset of technology and non-technology job descriptions collected from Kaggle."
    )

    st.dataframe(
        df.head(10),
        hide_index=True,
        use_container_width=True
    )

    st.divider()

    # -----------------------------
    # Footer
    # -----------------------------

    st.caption(
        "Developed using Python • Pandas • Plotly • Streamlit"
    )
    