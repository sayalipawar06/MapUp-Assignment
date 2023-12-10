import pandas as pd
from datetime import time, datetime, timedelta

def calculate_time_based_toll_rates(df):
    try:
        weekday_discounts = [
            (time(0, 0, 0), time(10, 0, 0), 0.8),
            (time(10, 0, 0), time(18, 0, 0), 1.2),
            (time(18, 0, 0), time(23, 59, 59), 0.8)
        ]
        weekend_discount = 0.7

        def apply_discount(row):
            current_time = row['start_time'].time()
            for start, end, discount in weekday_discounts:
                if start <= current_time <= end and row['start_day'] in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']:
                    return row * discount
            if row['start_day'] in ['Saturday', 'Sunday']:
                return row * weekend_discount
            return row

        df['start_day'] = df['start_timestamp'].dt.strftime('%A')
        df['start_time'] = df['start_timestamp'].dt.time
        df['end_day'] = df['end_timestamp'].dt.strftime('%A')
        df['end_time'] = df['end_timestamp'].dt.time

        vehicle_columns = ['moto', 'car', 'rv', 'bus', 'truck']
        for col in vehicle_columns:
            df[col] = df.apply(apply_discount, axis=1)

        return df

    except Exception as e:
        print(f"Error: {e}")
        return None

result_df = calculate_time_based_toll_rates(df)
if result_df is not None:
    print(result_df)