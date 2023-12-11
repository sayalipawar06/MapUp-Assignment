import pandas as pd

def find_ids_within_ten_percentage_threshold(input_path, reference_value):
    try:
        df = pd.read_csv(input_path)
        reference_df = df[df['id_start'] == reference_value]
        if not reference_df.empty:
            average_distance = reference_df['distance'].mean()
            lower_threshold = average_distance - 0.1 * average_distance
            upper_threshold = average_distance + 0.1 * average_distance

            within_threshold_df = df[(df['distance'] >= lower_threshold) & (df['distance'] <= upper_threshold)]
            result_ids = sorted(within_threshold_df['id_start'].unique())
            return result_ids
        
        else:
            print(f"No rows with 'id_start' value {reference_value} found.")
            return []
        
    except FileNotFoundError:
        print(f"Error: File not found at path '{input_path}'")
        return []

input_path = 'C:/Users/SAYALI PAWAR/MapUp-Data-Assessment-F/datasets/Question2-output.csv'
reference_value = 1001472
result_ids = find_ids_within_ten_percentage_threshold(input_path, reference_value)
print(result_ids)
