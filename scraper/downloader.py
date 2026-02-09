import requests
import logging
from time import sleep

MAX_RETRIES = 3

def download_file(url, output_path):
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            logging.info(f"Downloading file (Attempt {attempt})")
            response = requests.get(url, timeout=10)
            response.raise_for_status()

            with open(output_path, "wb") as f:
                f.write(response.content)

            logging.info("File downloaded successfully")
            return output_path

        except Exception as e:
            logging.error(f"Download failed: {e}")
            sleep(2)

    raise Exception("File download failed after retries")
