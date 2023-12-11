import pandas as pd

def generate_car_matrix(dataset_path):
    df = pd.read_csv(dataset_path)
    car_matrix = pd.pivot_table(df, values='car', index='id_1', columns='id_2', fill_value=0)

    # Set the diagonal values to 0
    for col in car_matrix.columns:
        car_matrix.at[col, col] = 0

    return car_matrix

dataset_path = 'C:/Users/SAYALI PAWAR/MapUp-Data-Assessment-F/datasets/dataset-1.csv'
result_matrix = generate_car_matrix(dataset_path)
print(result_matrix)
