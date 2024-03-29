## Data Pipeline Execution

The `main.py` script calls the `execute_data_pipeline` function, which is responsible for executing a data pipeline by invoking four other functions: `execute_json_place_holder_transformation` `execute_open_weather_transformation`, `execute_data_aggregation` and `write_to_database`

### Inputs
1. Sales data CSV file
2. JSONPlaceholder API
3. OpenWeatherMap API

### Flow

1. The `execute_data_pipeline` function first calls the `execute_json_place_holder_transformation` function.
2. The `execute_json_place_holder_transformation` function retrieves user data and sales data from a JSON placeholder API.
3. The retrieved data is merged into a single DataFrame.
4. The merged DataFrame is saved as a CSV file.
5. Next, the `execute_data_pipeline` function calls the `execute_open_weather_transformation` function.
6. The `execute_open_weather_transformation` function reads the previously saved CSV file.
7. The function selects the first 10 rows from the DataFrame.
8. Weather data for the selected rows is fetched using the OpenWeather API.
9. The weather data is merged with the selected DataFrame.
10. The final merged DataFrame is saved as another CSV file.
11. Then, it calls the execute_data_aggregation function, which reads the open_weather_transformation.csv file and performs various data aggregation operations, such as 
    i)Calculate total sales amount per customer.
    ii) Determine the average order quantity per product.
    iii) Identify the top-selling products or customers.
    iv) Analyze sales trends overtime(e.g.,monthlyorquarterlysales).
    v) Include weather data in the analysis(e.g.,average sales amount per weather condition).


### Outputs
12. Finally, it calls the write_to_database function, which writes the data to SQLite database tables. Table schemas are highlighted in tables.sql file.

### Usage Example
    Install packages mentioned in requirements.txt file 
    ```pip install -r requirements.txt``` , then run
    ```python main.py``` - This will provide visualization using matplotlib for aggregations

### Using Docker:
```docker build -t aiq_pipeline_image:latest .```
```docker run aiq_pipeline_image```
