import json
fp=open('data.json')
user_data=json.load(fp)

fcount=0

for user in user_data:
    if user['gender']=='Female':
        fcount=fcount+1
        
print("No of Female users:",fcount)

for user in user_data:
    if user['gender']=='Female':
        print(user['name'],":",user['email'],"-",user['gender'])
        
        
fp.close()