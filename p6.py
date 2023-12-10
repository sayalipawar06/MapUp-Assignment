import pandas as pd

def verify_timestamp_completeness(df):
    try:
        df['start_timestamp'] = pd.to_datetime(df['startDay'] + ' ' + df['startTime'], errors='coerce')
        df['end_timestamp'] = pd.to_datetime(df['endDay'] + ' ' + df['endTime'], errors='coerce')
    except Exception as e:
        print(f"Error during conversion: {e}")
        print(df[['startDay', 'startTime', 'endDay', 'endTime']]) 
        return None

    df['day_of_week'] = df['start_timestamp'].dt.dayofweek
    df['time'] = df['start_timestamp'].dt.time
    completeness_check = df.groupby(['id', 'id_2']).apply(check_timestamp_completeness)

    return completeness_check

def check_timestamp_completeness(group):
    full_day_coverage = group['time'].min() == pd.Timestamp('00:00:00').time() and group['time'].max() == pd.Timestamp('23:59:59').time()
    days_of_week_coverage = len(group['day_of_week'].unique()) == 7
    return pd.Series({'timestamp_completeness': full_day_coverage and days_of_week_coverage})

dataset_path = 'C:/Users/SAYALI PAWAR/MapUp-Data-Assessment-F/datasets/dataset-2.csv'
df = pd.read_csv(dataset_path)
completeness_result = verify_timestamp_completeness(df)
if completeness_result is not None:
    print(completeness_result)
