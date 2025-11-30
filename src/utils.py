# ======================================================
# Utility Functions: Logging + Saving Files
# ======================================================

import pandas as pd
from datetime import datetime

def log(message: str) -> None:
    """
    Print a log message with timestamp.
    """
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {message}")


def save_to_csv(df: pd.DataFrame, filename: str) -> None:
    """
    Save DataFrame to CSV file.
    """
    df.to_csv(filename, index=True)
    log(f"Data saved to file: {filename}")
