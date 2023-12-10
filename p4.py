import pandas as pd

def filter_routes(dataset_path):
    df = pd.read_csv(dataset_path)
    route_avg_truck = df.groupby('route')['truck'].mean()
    filtered_routes = route_avg_truck[route_avg_truck > 7].index.tolist()
    filtered_routes.sort()

    return filtered_routes

dataset_path = 'C:/Users/SAYALI PAWAR/MapUp-Data-Assessment-F/datasets/dataset-1.csv'
result = filter_routes(dataset_path)
print(result)
