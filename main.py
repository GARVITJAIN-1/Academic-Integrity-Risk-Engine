import pandas as pd
from datetime import datetime

# -------------------------------
# Core pipeline imports
# -------------------------------
from src.data_generation import generate_exam_data
from src.feature_engineering import engineer_features
from src.statistics_module import statistical_flags
from src.clustering import cluster_students
from src.anomaly_detection import anomaly_scores
from src.risk_scoring import calculate_risk

# Advanced features
from src.graph_similarity import build_similarity_graph
from src.explainability import generate_risk_reasons
from src.adaptive_thresholds import compute_dynamic_thresholds
from src.confidence_scoring import compute_confidence
from src.trend_analysis import compute_risk_trends

# -------------------------------
# STEP 1: Load / Generate Data
# -------------------------------
print("🔹 Generating exam data...")
df = generate_exam_data(n_students=1000)

# Add exam metadata (for trend analysis)
df["exam_id"] = "EXAM_001"
df["exam_date"] = datetime.today()

# -------------------------------
# STEP 2: Feature Engineering
# -------------------------------
print("🔹 Engineering features...")
df, df_scaled = engineer_features(df)

# -------------------------------
# STEP 3: Statistical Risk Flags
# -------------------------------
print("🔹 Computing statistical flags...")
df["stat_flag"] = statistical_flags(df)

# Store stats thresholds for explainability
stats_thresholds = {
    "fast_time": df["total_time"].mean() - 2 * df["total_time"].std(),
    "avg_time": df["total_time"].mean()
}

# -------------------------------
# STEP 4: Clustering (DBSCAN)
# -------------------------------
print("🔹 Clustering student behavior...")
df["cluster_label"] = cluster_students(df_scaled)

# -------------------------------
# STEP 5: Anomaly Detection
# -------------------------------
print("🔹 Running anomaly detection...")
df["anomaly_score"] = anomaly_scores(df_scaled)

# -------------------------------
# STEP 6: Graph-Based Similarity + Communities
# -------------------------------
print("🔹 Building similarity graph...")
df["similarity_risk"], community_map = build_similarity_graph(df_scaled)
df["community_id"] = df.index.map(lambda x: community_map.get(x, -1))

# -------------------------------
# STEP 7: Final Risk Scoring
# -------------------------------
print("🔹 Calculating risk scores...")
df["risk_score"] = calculate_risk(
    anomaly=df["anomaly_score"].values,
    stats=df["stat_flag"].values,
    similarity=df["similarity_risk"].values,
    cluster_labels=df["cluster_label"].values
)

# -------------------------------
# STEP 8: Adaptive Risk Thresholds
# -------------------------------
thresholds = compute_dynamic_thresholds(df["risk_score"])

def assign_risk_level(score):
    if score > thresholds["high"]:
        return "High"
    elif score > thresholds["medium"]:
        return "Medium"
    else:
        return "Low"

df["risk_level"] = df["risk_score"].apply(assign_risk_level)

# -------------------------------
# STEP 9: Confidence Scoring
# -------------------------------
df["confidence"] = compute_confidence(df["anomaly_score"].values)

# -------------------------------
# STEP 10: Explainability (Reasons)
# -------------------------------
print("🔹 Generating explainable reasons...")
df["risk_reasons"] = df.apply(
    lambda row: generate_risk_reasons(row, stats_thresholds),
    axis=1
)

# -------------------------------
# STEP 11: Risk Trend Analysis
# -------------------------------
print("🔹 Computing risk trends...")
df = compute_risk_trends(df)

# -------------------------------
# STEP 12: Save Final Output
# -------------------------------
output_path = "data/final/risk_results.csv"
df.to_csv(output_path, index=False)

print("✅ Pipeline executed successfully")
print(f"📁 Final results saved to: {output_path}")

# -------------------------------
# Optional: Display Summary
# -------------------------------
print("\n📊 Risk Level Distribution:")
print(df["risk_level"].value_counts())
