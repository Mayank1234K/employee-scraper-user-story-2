import logging
import re
import pandas as pd

COLUMN_MAPPING = {
    "id": "user_id",
    "userid": "user_id",
    "user id": "user_id",
    "user_id": "user_id",

    "firstname": "first_name",
    "first name": "first_name",
    "first_name": "first_name",

    "lastname": "last_name",
    "last name": "last_name",
    "last_name": "last_name",

    "email": "email",

    "gender": "sex",
    "sex": "sex",

    "jobtitle": "job_title",
    "job title": "job_title",
    "job_title": "job_title",

    "phone": "phone_number",
    "phonenumber": "phone_number",
    "phone number": "phone_number"
}

REQUIRED_FIELDS = ["user_id", "first_name", "last_name", "email"]
EMAIL_REGEX = r"[^@]+@[^@]+\.[^@]+"

def normalize_columns(df):
    new_cols = {}
    for col in df.columns:
        clean_col = col.replace("_", " ").strip()
        if clean_col in COLUMN_MAPPING:
            new_cols[col] = COLUMN_MAPPING[clean_col]
    return df.rename(columns=new_cols)

def validate_and_clean(df):
    df = normalize_columns(df)

    valid_records = []
    invalid = 0

    for _, row in df.iterrows():
        try:
            for field in REQUIRED_FIELDS:
                if field not in row or pd.isna(row[field]) or str(row[field]).strip() == "":
                    raise ValueError(f"Missing {field}")

            if not re.match(EMAIL_REGEX, str(row["email"])):
                raise ValueError("Invalid email format")

            record = {
                "user_id": row["user_id"],
                "first_name": str(row["first_name"]).strip().title(),
                "last_name": str(row["last_name"]).strip().title(),
                "sex": str(row.get("sex", "other")).lower(),
                "email": str(row["email"]).strip().lower(),
                "job_title": str(row.get("job_title", "")).strip(),
                "phone_number": str(row.get("phone_number", "")).strip()
            }

            valid_records.append(record)

        except Exception as e:
            invalid += 1
            logging.warning(f"Invalid record skipped: {e}")

    logging.info(f"Valid records: {len(valid_records)} | Invalid records: {invalid}")
    return valid_records
