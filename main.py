from scraper.processor import process_employee_data
from scraper.logger import setup_logger

URL = "https://drive.google.com/uc?id=1AWPf-pJodJKeHsARQK_RHiNsE8fjPCVK&export=download"
OUTPUT = "data/employees.csv"

def main():
    setup_logger()
    records = process_employee_data(URL, OUTPUT)
    print(f"Processed {len(records)} valid employee records")

if __name__ == "__main__":
    main()
