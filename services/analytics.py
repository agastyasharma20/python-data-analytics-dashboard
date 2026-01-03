import pandas as pd
from models.database import get_connection

def load_data(category=None):
    conn = get_connection()

    if category:
        query = "SELECT * FROM records WHERE category = ?"
        df = pd.read_sql(query, conn, params=(category,))
    else:
        df = pd.read_sql("SELECT * FROM records", conn)

    conn.close()
    return df


def get_summary(category=None):
    df = load_data(category)

    if df.empty:
        return None

    df["entry_index"] = range(1, len(df) + 1)
    category_counts = df["category"].value_counts()

    return {
        "average_score": round(df["score"].mean(), 2),
        "categories": category_counts.index.tolist(),
        "counts": category_counts.values.tolist(),
        "trend_x": df["entry_index"].tolist(),
        "trend_y": df["score"].tolist()
    }
def export_to_csv(category=None):
    df = load_data(category)
    file_name = "exported_data.csv"
    df.to_csv(file_name, index=False)
    return file_name

