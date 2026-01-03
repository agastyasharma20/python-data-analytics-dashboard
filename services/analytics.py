import pandas as pd
from models.database import get_connection

def load_data():
    conn = get_connection()
    df = pd.read_sql("SELECT * FROM records", conn)
    conn.close()
    return df

import pandas as pd
from models.database import get_connection

def load_data():
    conn = get_connection()
    df = pd.read_sql("SELECT * FROM records", conn)
    conn.close()
    return df

def get_summary():
    df = load_data()

    if df.empty:
        return None

    avg_score = round(df["score"].mean(), 2)
    category_counts = df["category"].value_counts()

    return {
        "average_score": avg_score,
        "categories": category_counts.index.tolist(),
        "counts": category_counts.values.tolist()
    }
