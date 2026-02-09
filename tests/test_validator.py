import pandas as pd
from scraper.validator import validate_and_clean

def test_validation():
    df = pd.DataFrame([{
        "user id": 1,
        "first name": " john ",
        "last name": " doe ",
        "email": "JOHN@TEST.COM",
        "sex": "Male",
        "job title": "Engineer",
        "phone": "1234567890"
    }])

    records = validate_and_clean(df)

    assert len(records) == 1
    assert records[0]["user_id"] == 1
    assert records[0]["first_name"] == "John"
    assert records[0]["last_name"] == "Doe"
    assert records[0]["email"] == "john@test.com"
def test_missing_or_invalid_data():
    df = pd.DataFrame([{
        "first name": "John",
        "last name": "Doe",
        "email": "john@test.com"
        # Missing user id
    }])

    records = validate_and_clean(df)

    assert records == []
