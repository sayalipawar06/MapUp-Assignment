import pandas as pd
import numpy as np

def calculate_distance_matrix(input_path):
    df = pd.read_csv(input_path)
    df = df.dropna(subset=['distance'])
    locations = set(df['id_start'].unique()).union(set(df['id_end'].unique()))
    distance_df = pd.DataFrame(index=locations, columns=locations)

    for index, row in df.iterrows():
        distance_df.at[row['id_start'], row['id_end']] = row['distance']
        distance_df.at[row['id_end'], row['id_start']] = row['distance']

    distance_df = distance_df.fillna(0)
    np.fill_diagonal(distance_df.values, 0)

    return distance_df

dataset_path = 'C:/Users/SAYALI PAWAR/MapUp-Data-Assessment-F/datasets/dataset-3.csv' 
distance_matrix = calculate_distance_matrix(dataset_path)
print(distance_matrix)
