# 🎓 Academic Integrity Risk Engine

An **explainable AI system** that detects **abnormal online exam behavior** using unsupervised machine learning, graph-based similarity analysis, and ethical risk scoring to support human review without making direct accusations.

---

## 📌 Problem Statement

With the rapid growth of online examinations, ensuring academic integrity at scale has become a major challenge. Traditional online proctoring solutions are often intrusive, costly, and difficult to scale, while automated cheating detection systems risk false accusations and ethical concerns.

In real-world scenarios, labeled cheating data is rarely available, making supervised approaches impractical. There is a strong need for an **ethical, explainable, and scalable AI-based solution** that can assist institutions without replacing human judgment.

---

## 🎯 Solution Overview

The **Academic Integrity Risk Engine** models **normal exam-taking behavior** and identifies **unusual behavioral patterns** using unsupervised learning.  
Instead of labeling students as cheaters, the system assigns:

- **Risk Score (0–100)**
- **Risk Level (Low / Medium / High)**
- **Explainable Reasons** for the risk
- **Confidence Score**
- **Behavioral Trends across multiple exams**

The system is designed strictly as a **decision-support tool**, ensuring that final decisions remain with human reviewers.

---

## 🚀 Key Features

- **Unsupervised Anomaly Detection** using Isolation Forest  
- **Behavioral Clustering** with DBSCAN  
- **Graph-Based Similarity Analysis** to identify potential collusion groups  
- **Explainable AI** with human-readable risk explanations  
- **Adaptive Risk Thresholds** based on exam-wide behavior  
- **Confidence-Aware Risk Scoring**  
- **Multi-Exam Risk Trend Analysis**  
- **Ethical, Human-in-the-Loop Design**  
- **Interactive Streamlit Dashboard** for visualization and analysis  

---

## 🧠 System Architecture
```text
Data Ingestion
      ↓
Feature Engineering
      ↓
Statistical Analysis
      ↓
Clustering & Anomaly Detection
      ↓
Graph-Based Similarity Analysis
      ↓
Risk Scoring Engine
      ↓
Explainability & Confidence Estimation
      ↓
Trend Analysis
      ↓
Dashboard Visualization



---

## 🛠 Tech Stack

- **Programming Language:** Python  
- **Data Processing:** Pandas, NumPy  
- **Machine Learning:** Scikit-learn  
- **Graph Analysis:** NetworkX  
- **Visualization & UI:** Streamlit  
- **ML Paradigm:** Unsupervised Learning  

---

## 📂 Project Structure

academic-integrity-risk-engine/
│
├── src/ # Core ML & logic modules
├── data/ # Raw, processed, and final datasets
├── app/ # Streamlit dashboard
├── main.py # End-to-end ML pipeline
├── requirements.txt # Project dependencies
├── .gitignore
└── README.md


---

## ▶️ How to Run Locally

### 1️⃣ Create Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate

2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Run the ML Pipeline
python main.py

4️⃣ Launch the Dashboard
streamlit run app/dashboard.py

📊 Dashboard Features

The Streamlit dashboard allows users to:

View individual risk scores and risk levels

Understand why a student is flagged

Compare a student’s behavior with the population

Analyze risk trends over time

Explore similarity and community-based patterns

⚠️ Ethical Considerations

This system does NOT label students as cheaters

Outputs are risk indicators, not final decisions

Designed to support human-in-the-loop review

Focuses on fairness, transparency, and explainability

Ethical AI principles were a core design goal throughout this project.
