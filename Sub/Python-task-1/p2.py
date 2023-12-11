import pandas as pd

def get_type_count(dataset_path):
    df = pd.read_csv(dataset_path)
    df['car_type'] = pd.cut(df['car'], bins=[-float('inf'), 15, 25, float('inf')],
                            labels=['low', 'medium', 'high'], right=False)
    type_counts = df['car_type'].value_counts().to_dict()
    sorted_type_counts = dict(sorted(type_counts.items()))

    return sorted_type_counts

dataset_path = 'C:/Users/SAYALI PAWAR/MapUp-Data-Assessment-F/datasets/dataset-1.csv'
result = get_type_count(dataset_path)
print(result)
