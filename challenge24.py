import pandas as pd

def quarter_volume():
    data = pd.read_csv('apple.csv', header=0)
    new_data = pd.Series(list(data.Volume), index=pd.to_datetime(data.Date))
    result = new_data.resample('Q').sum()
    sort_result = result.sort_values(ascending=False)
    second_volume = sort_result[1]
    return second_volume

if __name__ == '__main__':
    print(quarter_volume())
