def compute_dynamic_thresholds(risk_scores):
    mean = risk_scores.mean()
    std = risk_scores.std()

    return {
        "low": mean - std,
        "medium": mean + std,
        "high": mean + 2 * std
    }
