import streamlit as st
import pandas as pd
import ast
import os

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.append(PROJECT_ROOT)

from main import run_pipeline# ✅ IMPORTANT

# -------------------------------
# Load Data
# -------------------------------
@st.cache_data
def load_data():
    data_path = "data/final/risk_results.csv"

    # Ensure directory exists
    os.makedirs("data/final", exist_ok=True)

    # If file doesn't exist, run pipeline safely
    if not os.path.exists(data_path):
        st.warning("Risk data not found. Running ML pipeline...")
        run_pipeline()

    return pd.read_csv(data_path)


df = load_data()

st.set_page_config(page_title="Academic Integrity Risk Engine", layout="wide")

# -------------------------------
# Title
# -------------------------------
st.title("🎓 Academic Integrity Risk Engine")
st.markdown(
    "This dashboard shows **risk-based, explainable insights** into online exam behavior. "
    "The system does NOT accuse students — it highlights **unusual patterns** for review."
)

# -------------------------------
# Sidebar Controls
# -------------------------------
st.sidebar.header("🔍 Student Selection")
student_id = st.sidebar.selectbox(
    "Select Student ID",
    df["student_id"].unique()
)

student = df[df["student_id"] == student_id].iloc[0]

# -------------------------------
# Main Metrics
# -------------------------------
col1, col2, col3 = st.columns(3)

col1.metric("Risk Score", round(student["risk_score"], 2))
col2.metric("Risk Level", student["risk_level"])
col3.metric("Confidence (%)", round(student["confidence"], 2))

# -------------------------------
# Explainability Section
# -------------------------------
st.subheader("🧠 Risk Explanation")

try:
    reasons = ast.literal_eval(student["risk_reasons"])
except Exception:
    reasons = []

if reasons:
    for reason in reasons:
        st.warning(reason)
else:
    st.success("No unusual behavior detected.")

# -------------------------------
# Behavioral Comparison
# -------------------------------
st.subheader("📊 Student vs Population Comparison")

comparison_df = pd.DataFrame({
    "Metric": ["Total Time", "Score %", "Answer Changes"],
    "Student": [
        student["total_time"],
        student["score_percentage"],
        student["answer_changes"]
    ],
    "Population Average": [
        df["total_time"].mean(),
        df["score_percentage"].mean(),
        df["answer_changes"].mean()
    ]
})

st.dataframe(comparison_df, use_container_width=True)

# -------------------------------
# Risk Trend (if multiple exams)
# -------------------------------
st.subheader("📈 Risk Trend Over Time")

student_trend = df[df["student_id"] == student_id]

if "risk_trend" in student_trend.columns and len(student_trend) > 1:
    st.line_chart(student_trend.set_index("exam_date")["risk_trend"])
else:
    st.info("Trend data available when multiple exams are present.")

# -------------------------------
# Community / Similarity Info
# -------------------------------
st.subheader("🧩 Similarity & Community Analysis")

st.write(f"**Similarity Risk Score:** {student['similarity_risk']}")
st.write(f"**Community ID:** {student['community_id']}")

# -------------------------------
# Global Risk Distribution
# -------------------------------
st.subheader("🌍 Overall Risk Distribution")
st.bar_chart(df["risk_score"])

# -------------------------------
# Footer
# -------------------------------
st.markdown("---")
st.caption(
    "⚠️ This system provides decision support only. "
    "Final judgments should always be made by human reviewers."
)
