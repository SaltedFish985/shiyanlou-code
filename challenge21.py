import json
import pandas as pd

def analysis(file, user_id):
    times = 0
    minutes = 0
    df = pd.read_json(file, orient='records')
    times = len(df[df['user_id'] == user_id])
    minutes = df[df['user_id'] == user_id]['minutes'].sum()
    return times, minutes

if __name__ == '__main__':
	filename = '/home/shiyanlou/Code/user_study.json'
	user_id = 199805
	times, minutes = analysis(filename, user_id)
	print("times: ", times)
	print("minutes: ", minutes)