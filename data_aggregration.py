import pandas as pd
import matplotlib.pyplot as plt


def total_sales_per_customer(df):
    df["total_sales"] = df["quantity"] * df["price"]
    total_sales_df = df.groupby("customer_id")["total_sales"].sum()
    ax = plt.subplot()
    total_sales_df.plot(x="customer_id", y="total_sales", kind="bar", ax=ax, title="Customer Total Sales")
    plt.show()


def average_product_quantity(df):
    average_product_quantity_df = df.groupby("product_id")["quantity"].mean()
    ax = plt.subplot()
    average_product_quantity_df.plot(x="product_id", y="quantity", kind="bar", ax=ax, title="Average Product Quantity")
    plt.show()


def top_selling_product(df):
    average_product_quantity_df = df.groupby("product_id")["quantity"].sum()
    average_product_df = average_product_quantity_df.to_frame().reset_index()
    top_products = average_product_df[average_product_df["quantity"] == average_product_df["quantity"].max()].reset_index()
    ax = plt.subplot()
    ax.axis('off')
    ax.text(x=0.5, y=0.5, size=25, ha="center", s=f"Top Selling Product is {top_products['product_id'][0]}")
    plt.show()


def top_purchasing_customers(df):
    df["total_sales"] = df["quantity"] * df["price"]
    total_sales_df = df.groupby("customer_id")["total_sales"].sum()
    top_customers_df = total_sales_df.to_frame().reset_index()
    top_customers = top_customers_df[top_customers_df["total_sales"] == top_customers_df["total_sales"].max()].reset_index()
    ax = plt.subplot()
    ax.axis('off')
    ax.text(x=0.5, y=0.5, size=25, ha="center", s=f"Top Purchasing Customer is {top_customers['customer_id'][0]}")
    plt.show()


def sales_trend(df):
    df["total_sales"] = df["quantity"] * df["price"]
    total_sales_df = df.groupby("order_date")["total_sales"].sum()
    ax = plt.subplot()
    total_sales_df.plot(x="order_date", y="total_sales", kind="line", ax=ax, title="Sales Trend Daily")
    plt.show()

    df["order_date"] = pd.to_datetime(df["order_date"])
    total_sales_df = df.groupby(df.order_date.dt.month)["total_sales"].sum()
    ax1 = plt.subplot()
    total_sales_df.plot(x="order_date", y="total_sales", kind="line", ax=ax1, title="Sales Trend Monthly")
    plt.show()

    total_sales_df = df.groupby(df.order_date.dt.year)["total_sales"].sum()
    ax1 = plt.subplot()
    total_sales_df.plot(x="order_date", y="total_sales", kind="line", ax=ax1, title="Sales Trend Yearly")
    plt.show()


def weather_trend(df):
    df["total_sales"] = df["quantity"] * df["price"]
    total_sales_df = df.groupby("weather_condition")["total_sales"].sum()
    ax = plt.subplot()
    total_sales_df.plot(x="weather_condition", y="total_sales", kind="bar", ax=ax, title="Weather Trend")
    plt.show()
