import pandas as pd

def get_bus_indexes(dataset_path):
    df = pd.read_csv(dataset_path)
    mean_bus_value = df['bus'].mean()
    bus_indexes = df[df['bus'] > 2 * mean_bus_value].index.tolist()
    bus_indexes.sort()

    return bus_indexes

dataset_path = 'C:/Users/SAYALI PAWAR/MapUp-Data-Assessment-F/datasets/dataset-1.csv'
result = get_bus_indexes(dataset_path)
print(result)
