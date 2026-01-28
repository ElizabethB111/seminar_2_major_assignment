from pathlib import Path
from loguru import logger
from tqdm import tqdm
import typer
import pandas as pd

from seminar_2_major_assignment.config import PROCESSED_DATA_DIR, RAW_DATA_DIR

app = typer.Typer()

@app.command()
def main(
    input_path: Path = RAW_DATA_DIR / "dataset.csv",
    output_path: Path = PROCESSED_DATA_DIR / "dataset.csv",
):
    logger.info("Processing dataset...")

    df = pd.read_csv(input_path)

    if "unnecessary_column" in df.columns:
        df = df.drop(columns=["unnecessary_column"])

    if "old_name" in df.columns:
        df = df.rename(columns={"old_name": "new_name"})

    if "achievement_percentage" in df.columns:
        df = df[df["achievement_percentage"] > 0]

    output_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_path, index=False)

    logger.success(f"Processed dataset saved to {output_path}")

if __name__ == "__main__":
    app()
