import numpy as np

def statistical_flags(df):
    flags = []

    time_mean = df["total_time"].mean()
    time_std = df["total_time"].std()

    for _, row in df.iterrows():
        flag = 0
        if row["total_time"] < time_mean - 2*time_std:
            flag += 1
        if row["score_percentage"] > 90 and row["total_time"] < time_mean:
            flag += 1
        if row["answer_changes"] > df["answer_changes"].quantile(0.95):
            flag += 1
        flags.append(flag)

    return np.array(flags)
