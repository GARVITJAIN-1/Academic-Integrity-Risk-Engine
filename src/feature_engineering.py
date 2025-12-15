import pandas as pd
from sklearn.preprocessing import StandardScaler

def engineer_features(df):
    df = df.copy()

    df["speed_score"] = df["score_percentage"] / df["total_time"]
    df["consistency_ratio"] = df["std_time_per_question"] / df["avg_time_per_question"]
    df["change_rate"] = df["answer_changes"] / df["total_time"]

    features = [
        "total_time", "avg_time_per_question",
        "std_time_per_question", "score_percentage",
        "answer_changes", "submission_delay",
        "device_switch_count", "speed_score",
        "consistency_ratio", "change_rate"
    ]

    scaler = StandardScaler()
    df_scaled = scaler.fit_transform(df[features])

    return df, df_scaled
