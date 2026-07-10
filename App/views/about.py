import streamlit as st


def show_about():

    st.title("ℹ️ About")

    st.markdown("""
# 🎯 Career Skills Intelligence Platform

Welcome to the **Career Skills Intelligence Platform**, an interactive dashboard built to help students and job seekers make informed career decisions using job market data.

---

## 🚀 Project Objective

This application analyzes real-world job descriptions to:

- 📊 Identify in-demand skills
- 📈 Understand career progression
- 🎯 Analyze skill gaps
- 📚 Recommend skills to learn

---

## ✨ Features

### 🏠 Home
Overview of the project with key statistics and insights.

### 📊 Market Analysis
- Top Job Roles
- Most In-demand Skills
- Experience Distribution
- Market Trends

### 📈 Career Progression
Analyze how required skills change with different experience levels.

### 🎯 Skill Gap Analyzer
- Compare your skills with job requirements
- View Match Score
- Identify Missing Skills
- Get a Learning Roadmap

---

## 🛠 Technologies Used

- Python
- Streamlit
- Pandas
- Plotly
- NumPy

---

## 📂 Dataset

**Source:** Kaggle Job Descriptions Dataset

The dataset contains job descriptions from various industries and includes:

- Job Titles
- Experience Levels
- Required Skills
- Responsibilities

---

## 👩‍💻 Developer

**Naveli Gupta**

B.Tech - Production & Industrial Engineering

Motilal Nehru National Institute of Technology (MNNIT)

---

## 🌟 Future Enhancements

- Resume Analyzer
- AI Career Recommendations
- Salary Prediction
- Course Recommendations
- Live Job API Integration

---

### Thank you for visiting the Career Skills Intelligence Platform! 🚀
""")