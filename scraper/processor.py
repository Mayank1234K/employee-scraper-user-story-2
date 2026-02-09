import logging
from scraper.downloader import download_file
from scraper.parser import parse_file
from scraper.validator import validate_and_clean

def process_employee_data(url, output_path):
    file_path = download_file(url, output_path)
    df = parse_file(file_path)
    records = validate_and_clean(df)
    return records
