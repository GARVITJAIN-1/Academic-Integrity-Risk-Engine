import numpy as np
import pandas as pd

def generate_exam_data(n_students=1000, random_state=42):
    np.random.seed(random_state)

    data = {
        "student_id": range(n_students),
        "total_time": np.random.normal(3600, 600, n_students),  # seconds
        "avg_time_per_question": np.random.normal(60, 15, n_students),
        "std_time_per_question": np.random.normal(12, 4, n_students),
        "score_percentage": np.random.normal(70, 10, n_students),
        "answer_changes": np.random.poisson(5, n_students),
        "submission_delay": np.random.normal(0, 300, n_students),
        "device_switch_count": np.random.poisson(1, n_students)
    }

    df = pd.DataFrame(data)

    # Inject anomalies (cheating-like behavior)
    anomaly_idx = np.random.choice(n_students, int(0.05*n_students), replace=False)
    df.loc[anomaly_idx, "total_time"] *= 0.4
    df.loc[anomaly_idx, "score_percentage"] += 25
    df.loc[anomaly_idx, "answer_changes"] += 15

    df.to_csv("data/exam_data.csv", index=False)
    return df
