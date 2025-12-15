def compute_risk_trends(df):
    df = df.sort_values(by=["student_id", "exam_date"])
    df["risk_trend"] = (
        df.groupby("student_id")["risk_score"]
        .rolling(window=3, min_periods=1)
        .mean()
        .reset_index(level=0, drop=True)
    )
    return df
