import pandas as pd

def multiply_matrix(input_path):
    df = pd.read_csv(input_path, index_col=0)
    df = df.apply(pd.to_numeric, errors='coerce')
    modified_df = df.copy()
    for column in modified_df.columns:
        for index in modified_df.index:
            value = modified_df.at[index, column]

            if not pd.isna(value):
                if value > 20:
                    modified_df.at[index, column] = round(value * 0.75, 1)
                else:
                    modified_df.at[index, column] = round(value * 1.25, 1)

    return modified_df

input_path = 'C:/Users/SAYALI PAWAR/MapUp-Data-Assessment-F/datasets/datasets1-output.csv'
result_df_modified = multiply_matrix(input_path)
print(result_df_modified)
