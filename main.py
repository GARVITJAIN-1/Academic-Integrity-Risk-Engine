import os
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


def run_pipeline(n_students=1000):
    """
    Runs the complete Academic Integrity Risk Engine pipeline
    and saves the final risk results.
    """

    print("🔹 Starting Academic Integrity Risk Engine pipeline...")

    # Ensure output directory exists (important for cloud)
    os.makedirs("data/final", exist_ok=True)

    # -------------------------------
    # STEP 1: Load / Generate Data
    # -------------------------------
    df = generate_exam_data(n_students=n_students)

    df["exam_id"] = "EXAM_001"
    df["exam_date"] = datetime.today()

    # -------------------------------
    # STEP 2: Feature Engineering
    # -------------------------------
    df, df_scaled = engineer_features(df)

    # -------------------------------
    # STEP 3: Statistical Risk Flags
    # -------------------------------
    df["stat_flag"] = statistical_flags(df)

    stats_thresholds = {
        "fast_time": df["total_time"].mean() - 2 * df["total_time"].std(),
        "avg_time": df["total_time"].mean()
    }

    # -------------------------------
    # STEP 4: Clustering
    # -------------------------------
    df["cluster_label"] = cluster_students(df_scaled)

    # -------------------------------
    # STEP 5: Anomaly Detection
    # -------------------------------
    df["anomaly_score"] = anomaly_scores(df_scaled)

    # -------------------------------
    # STEP 6: Graph-Based Similarity
    # -------------------------------
    df["similarity_risk"], community_map = build_similarity_graph(df_scaled)
    df["community_id"] = df.index.map(lambda x: community_map.get(x, -1))

    # -------------------------------
    # STEP 7: Risk Scoring
    # -------------------------------
    df["risk_score"] = calculate_risk(
        anomaly=df["anomaly_score"].values,
        stats=df["stat_flag"].values,
        similarity=df["similarity_risk"].values,
        cluster_labels=df["cluster_label"].values
    )

    # -------------------------------
    # STEP 8: Adaptive Thresholds
    # -------------------------------
    thresholds = compute_dynamic_thresholds(df["risk_score"])

    df["risk_level"] = df["risk_score"].apply(
        lambda x: "High" if x > thresholds["high"]
        else "Medium" if x > thresholds["medium"]
        else "Low"
    )

    # -------------------------------
    # STEP 9: Confidence Scoring
    # -------------------------------
    df["confidence"] = compute_confidence(df["anomaly_score"].values)

    # -------------------------------
    # STEP 10: Explainability
    # -------------------------------
    df["risk_reasons"] = df.apply(
        lambda row: generate_risk_reasons(row, stats_thresholds),
        axis=1
    )

    # -------------------------------
    # STEP 11: Trend Analysis
    # -------------------------------
    df = compute_risk_trends(df)

    # -------------------------------
    # STEP 12: Save Output
    # -------------------------------
    output_path = "data/final/risk_results.csv"
    df.to_csv(output_path, index=False)

    print("✅ Pipeline executed successfully")
    print(f"📁 Results saved to: {output_path}")

    return df


# Allow local execution
if __name__ == "__main__":
    run_pipeline()
