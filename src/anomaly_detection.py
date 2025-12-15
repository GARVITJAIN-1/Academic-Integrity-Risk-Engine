from sklearn.ensemble import IsolationForest

def anomaly_scores(df_scaled):
    model = IsolationForest(contamination=0.05, random_state=42)
    model.fit(df_scaled)
    scores = -model.decision_function(df_scaled)
    return scores
