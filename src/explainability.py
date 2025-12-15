def generate_risk_reasons(row, stats_thresholds):
    reasons = []

    if row["total_time"] < stats_thresholds["fast_time"]:
        reasons.append("Unusually fast exam completion")

    if row["score_percentage"] > 90 and row["total_time"] < stats_thresholds["avg_time"]:
        reasons.append("High score achieved in short duration")

    if row["similarity_risk"] > 5:
        reasons.append("High answer similarity with multiple peers")

    if row["cluster_label"] == -1:
        reasons.append("Behavior deviates significantly from majority")

    if row["device_switch_count"] > 2:
        reasons.append("Multiple device switches during exam")

    return reasons
