import pandas as pd
from matplotlib import pyplot as plt

def data_plot():
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    df = pd.read_json("/home/shiyanlou/Code/user_study.json", orient="records")
    user_set = set(df['user_id'])
    user_list = []
    minutes_list = []
    data = []
    for the_user in user_set:
        minutes = df[df['user_id'] == the_user]['minutes'].sum()
        data.append((the_user, minutes))
    data.sort()
    for num in data:
        user_list.append(num[0])
        minutes_list.append(num[1])
    ax.set_title("StudyData")
    ax.set_xlabel("User ID")
    ax.set_ylabel("Study Time")
    ax.plot(user_list, minutes_list)
    plt.show()
    return ax

if __name__ == '__main__':
    data_plot()