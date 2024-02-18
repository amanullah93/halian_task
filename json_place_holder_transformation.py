import pandas as pd
import utility

USER_API_URL = "https://jsonplaceholder.typicode.com/users"
SALES_DATA_FILE_NAME = "AIQ - Data Engineer Assignment - Sales data.csv"
MERGE_KEY = "customer_id"


def parse_user_data(users):
    parsed_users = []
    for user in users:
        parsed_users.append({
            "customer_id": user["id"],
            "name": user["name"],
            "user_name": user["username"],
            "email": user["email"],
            "lat": user["address"]["geo"]["lat"],
            "lng": user["address"]["geo"]["lng"]
        })
    return parsed_users


def merge_sales_and_user_data(user_data, sales_data):
    merged_df = sales_data.merge(user_data, on=MERGE_KEY)
    return merged_df


def fetch_sales_data():
    sales_df = pd.read_csv(SALES_DATA_FILE_NAME)
    return sales_df


def fetch_user_data():
    users = utility.fetch_data_from_api(USER_API_URL)
    parsed_users = parse_user_data(users)
    return pd.DataFrame.from_dict(parsed_users)