import streamlit as st
from collections import Counter


def show_skill_gap(df):

    st.title("🎯 Skill Gap Analyzer")

    st.markdown(
        "Compare your current skills with the requirements of your target role."
    )

    st.divider()

    # =====================================
    # Search Target Role
    # =====================================

    search_role = st.text_input(
        "🔍 Search Job Role",
        placeholder="Type a job role..."
    )

    roles = sorted(df["Title"].dropna().unique())

    if search_role:

        roles = [
            role
            for role in roles
            if search_role.lower() in role.lower()
        ]

    selected_role = st.selectbox(
        "🎯 Select Target Role",
        roles
    )

    st.divider()

    # =====================================
    # Searchable Skill Selector
    # =====================================

    all_skills = sorted(
        list(
            set(
                sum(df["Skills_list"], [])
            )
        )
    )

    user_skills = st.multiselect(
        "🛠 Select Your Skills",
        options=all_skills,
        placeholder="Search and select your skills..."
    )

    st.divider()

    # =====================================
    # Analyze Button
    # =====================================

    if st.button(
        "🚀 Analyze Skill Gap",
        use_container_width=True
    ):

        role_df = df[df["Title"] == selected_role]

        role_skills = sum(
            role_df["Skills_list"],
            []
        )

        required_skills = [
            skill
            for skill, count in Counter(role_skills).most_common(10)
        ]

        matched = []

        missing = []

        for skill in required_skills:

            if skill.lower() in [
                s.lower()
                for s in user_skills
            ]:

                matched.append(skill)

            else:

                missing.append(skill)

        score = round(
            len(matched) /
            len(required_skills) * 100,
            1
        ) 
                # =====================================
        # KPI Cards
        # =====================================

        st.subheader("📊 Skill Gap Summary")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                "🎯 Match Score",
                f"{score}%"
            )

        with col2:
            st.metric(
                "✅ Skills Matched",
                len(matched)
            )

        with col3:
            st.metric(
                "❌ Skills Missing",
                len(missing)
            )

        st.progress(score / 100)

        st.divider()

        # =====================================
        # Placement Remark
        # =====================================

        if score >= 90:

            st.success("🟢 Excellent Match! You are placement ready.")

        elif score >= 75:

            st.success("🟢 Very Good Match! Only a few skills are missing.")

        elif score >= 60:

            st.warning("🟡 Good Match! Improve a few important skills.")

        elif score >= 40:

            st.warning("🟠 Needs Improvement. Focus on the missing skills.")

        else:

            st.error("🔴 Beginner. Build your fundamentals first.")

        st.divider()

        # =====================================
        # Skills Comparison
        # =====================================

        left, right = st.columns(2)

        with left:

            st.subheader("✅ Skills You Have")

            if matched:

                for skill in matched:
                    st.success(skill)

            else:

                st.info("No matching skills.")

        with right:

            st.subheader("❌ Skills Missing")

            if missing:

                for skill in missing:
                    st.error(skill)

            else:

                st.success("No missing skills!")

        st.divider()

        # =====================================
        # Learning Roadmap
        # =====================================

        st.subheader("📚 Learning Roadmap")

        if missing:

            for i, skill in enumerate(missing, start=1):

                st.write(
                    f"**Step {i}:** Learn **{skill}**"
                )

        else:

            st.success(
                "🎉 Congratulations! You already have all the key skills for this role."
            )
            