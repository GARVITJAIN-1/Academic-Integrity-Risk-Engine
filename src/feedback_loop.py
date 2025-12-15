def adjust_weights(feedback, weights):
    if feedback == "false_positive":
        weights["anomaly"] *= 0.9
    elif feedback == "confirmed":
        weights["anomaly"] *= 1.1
    return weights
