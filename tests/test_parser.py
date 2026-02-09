import pandas as pd
from scraper.parser import parse_file

def test_csv_file_extraction(tmp_path):
    file = tmp_path / "employees.csv"
    file.write_text(
        "user id,first name,last name,email\n"
        "1,John,Doe,john@test.com"
    )

    df = parse_file(str(file))

    assert isinstance(df, pd.DataFrame)
    assert len(df) == 1
import pytest
from scraper.parser import parse_file

def test_invalid_file_format(tmp_path):
    file = tmp_path / "employees.txt"
    file.write_text("invalid content")

    with pytest.raises(Exception):
        parse_file(str(file))
