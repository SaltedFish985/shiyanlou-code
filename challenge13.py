import sys
from pymongo import MongoClient

def get_rank(user_id):
    client = MongoClient()
    db = client.shiyanlou
    contests = db.contests
    id_set = set()
    for num in contests.find():
        id_set.add(num['user_id'])
    id_list = list(id_set)
    result_list = []
    for userid in id_list:
        the_score = 0
        the_time = 0
        for num in contests.find({'user_id':userid}):
            the_score += num['score'] 
            the_time += num['submit_time']
        result_list.append((userid, the_score, the_time))     
    result_list.sort(key=lambda x:(x[1],x[2]), reverse=True)
    temp = (0,0,0)
    for index in range(len(result_list)-1):
        if result_list[index][2] > result_list[index+1][2] and result_list[index][1] == result_list[index+1][1]:
            temp = result_list[index]
            result_list[index] = result_list[index+1]
            result_list[index+1] = temp                
    rank = 0
    score = 0
    submit_time =0
    flag = 1
    for num in result_list:
        if user_id == num[0]:
            rank = result_list.index(num)+1
            score = num[1]
            submit_time = num[2]
            flag = 0
            break
    if flag == 1:
        print("NOTFOUND")
        exit()
    return rank, score, submit_time

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Parameter Error")
        exit()
    try:
        user_id = int(sys.argv[1])
    except:
        print("Parameter Error")
        exit()    
    userdata = get_rank(user_id)
    print(userdata)