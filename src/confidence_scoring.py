import numpy as np

def compute_confidence(anomaly_scores):
    normalized = (anomaly_scores - anomaly_scores.min()) / (
        anomaly_scores.max() - anomaly_scores.min()
    )
    confidence = 1 - normalized
    return np.round(confidence * 100, 2)
