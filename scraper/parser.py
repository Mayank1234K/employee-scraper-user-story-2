import pandas as pd
import logging
import os

SUPPORTED_EXTENSIONS = [".csv", ".xlsx"]

def parse_file(file_path):
    try:
        _, ext = os.path.splitext(file_path)

        if ext.lower() not in SUPPORTED_EXTENSIONS:
            raise ValueError(f"Unsupported file format: {ext}")

        if ext.lower() == ".csv":
            logging.info("Parsing CSV file")
            df = pd.read_csv(
                file_path,
                header=0,
                skip_blank_lines=True
            )

        elif ext.lower() == ".xlsx":
            logging.info("Parsing Excel file")
            df = pd.read_excel(file_path)

        # Normalize column names
        df.columns = (
            df.columns
            .str.strip()
            .str.lower()
        )

        logging.info(f"Detected columns: {list(df.columns)}")
        return df

    except Exception as e:
        logging.error(f"Parsing error: {e}")
        raise
