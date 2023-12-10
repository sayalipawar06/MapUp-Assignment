import pandas as pd

def unroll_distance_matrix(input_path):
    distance_matrix = pd.read_csv(input_path, index_col=0)
    id_start_list = []
    id_end_list = []
    distance_list = []

    for id_start in distance_matrix.index:
        for id_end in distance_matrix.columns:
            if id_start != id_end:
                id_start_list.append(id_start)
                id_end_list.append(id_end)
                distance_list.append(distance_matrix.at[id_start, id_end])

    unrolled_df = pd.DataFrame({'id_start': id_start_list, 'id_end': id_end_list, 'distance': distance_list})
    return unrolled_df

dataset_path = 'C:/Users/SAYALI PAWAR/MapUp-Data-Assessment-F/datasets/datasets3-output.csv'
unrolled_df = unroll_distance_matrix(dataset_path)
print(unrolled_df)
