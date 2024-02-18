import json_place_holder_transformation
import open_weather_transformation
import data_aggregration
import db_engine

import pandas as pd


JSON_PLACEHOLDER_FILE_NAME = "json_place_holder_transformation.csv"
OPEN_WEATHER_TRANSFORMATION_FILE_NAME = "open_weather_transformation.csv"


def execute_json_place_holder_transformation():
    user_df = json_place_holder_transformation.fetch_user_data()
    sales_df = json_place_holder_transformation.fetch_sales_data()
    merged_df = json_place_holder_transformation.merge_sales_and_user_data(user_df, sales_df)
    merged_df.to_csv(JSON_PLACEHOLDER_FILE_NAME, index=None)


def execute_open_weather_transformation():
    df = pd.read_csv(JSON_PLACEHOLDER_FILE_NAME)
    weather_df = open_weather_transformation.get_weather_for_orders(df)
    final_df = open_weather_transformation.merge_sales_and_weather_data(weather_df, df)
    final_df.to_csv(OPEN_WEATHER_TRANSFORMATION_FILE_NAME, index=None)


def execute_data_aggregation():
    df = pd.read_csv(OPEN_WEATHER_TRANSFORMATION_FILE_NAME)
    data_aggregration.total_sales_per_customer(df)
    data_aggregration.average_product_quantity(df)
    data_aggregration.top_selling_product(df)
    data_aggregration.top_purchasing_customers(df)
    data_aggregration.sales_trend(df)
    data_aggregration.weather_trend(df)


def write_to_database():
    df = pd.read_csv(OPEN_WEATHER_TRANSFORMATION_FILE_NAME)
    db_engine.write_to_database(df)


def execute_data_pipeline():
    execute_json_place_holder_transformation()
    execute_open_weather_transformation()
    execute_data_aggregation()
    write_to_database()


if __name__ == '__main__':
    execute_data_pipeline()
