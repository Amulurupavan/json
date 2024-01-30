#read data.json(100 records)
import json
fp=open('data.json','r')
user_data=json.load(fp)
#print(user_data)
print(len(user_data))


for user in user_data:
    if user['gender']=='Male':
        print(user['name'],":",user['email'],"-",user['gender'])