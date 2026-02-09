from unittest.mock import patch
from scraper.downloader import download_file

@patch("scraper.downloader.requests.get")
def test_csv_file_download(mock_get, tmp_path):
    mock_get.return_value.status_code = 200
    mock_get.return_value.content = b"id,first name\n1,John"

    output = tmp_path / "employees.csv"
    result = download_file("http://fake-url", str(output))

    assert output.exists()
    assert result == str(output)
