import pandas as pd

def calculate_toll_rate(input_path):
    try:
        df = pd.read_csv(input_path)
        df['distance'] = pd.to_numeric(df['distance'], errors='coerce')

        rate_coefficients = {
            'moto': 0.8,
            'car': 1.2,
            'rv': 1.5,
            'bus': 2.2,
            'truck': 3.6
        }

        for vehicle_type, rate_coefficient in rate_coefficients.items():
            df[vehicle_type] = df['distance'] * rate_coefficient

        return df
    
    except FileNotFoundError:
        print(f"Error: File not found at path '{input_path}'")
        return None

input_path = 'C:/Users/SAYALI PAWAR/MapUp-Data-Assessment-F/datasets/Question2-output.csv'
result_df = calculate_toll_rate(input_path)
if result_df is not None:
    print(result_df)
