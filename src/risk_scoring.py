import numpy as np

def calculate_risk(anomaly, stats, similarity, cluster_labels):
    risk_scores = []

    for i in range(len(anomaly)):
        risk = (
            0.4 * anomaly[i] +
            0.3 * stats[i] +
            0.2 * similarity[i] +
            0.1 * (1 if cluster_labels[i] == -1 else 0)
        )
        risk_scores.append(risk * 100)

    return np.array(risk_scores)
