from sklearn.cluster import DBSCAN

def cluster_students(df_scaled):
    model = DBSCAN(eps=1.5, min_samples=10)
    labels = model.fit_predict(df_scaled)
    return labels
