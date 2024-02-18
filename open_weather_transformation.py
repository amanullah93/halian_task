import random
import math
import utility
import pandas as pd


OPEN_WEATHER_API_URL = "https://api.openweathermap.org/data/2.5/weather?"
OPEN_WEATHER_API_KEY = "ab1a190f731c0466744dc8e0c9109346"
MERGE_KEY= "order_id"


def generate_random_coordinates():
    radius = 1000000
    radius_in_degree = radius/111300
    x0 = 40.84
    y0 = -73.87
    u = float(random.uniform(0.0, 1.0))
    v = float(random.uniform(0.0, 1.0))
    w = radius_in_degree * math.sqrt(u)
    t = 2 * math.pi * v
    x = w * math.cos(t)
    y = w * math.sin(t)
    lat = round(x + x0, 6)
    lng = round(y + y0, 6)
    return {"lat": str(lat), "lng": str(lng)}


def get_weather_info_from_open_weather(lat, lng, order_id):
    url = f"{OPEN_WEATHER_API_URL}lat={lat}&lon={lng}&appid={OPEN_WEATHER_API_KEY}"
    weather_info = utility.fetch_data_from_api(url)
    print(weather_info)
    return {
        "order_id": order_id,
        "temp": weather_info["main"]["temp"],
        "temp_min": weather_info["main"]["temp_min"],
        "temp_max": weather_info["main"]["temp_max"],
        "pressure": weather_info["main"]["pressure"],
        "humidity": weather_info["main"]["humidity"],
        "wind_speed": weather_info["wind"]["speed"],
        "wind_deg": weather_info["wind"]["deg"],
        "weather_condition": weather_info["weather"][0]["description"],
        "store_lat": lat,
        "store_lng": lng
    }


def get_weather_for_orders(df):
    weather_info = []
    for i in range(0, df.shape[0]):
        lat_lng = generate_random_coordinates()
        weather_info.append(
            get_weather_info_from_open_weather(lat_lng["lat"], lat_lng["lng"], df["order_id"][i])
        )
    return pd.DataFrame.from_dict(weather_info)


def merge_sales_and_weather_data(weather_data, sales_data):
    merged_df = sales_data.merge(weather_data, on=MERGE_KEY)
    return merged_df

