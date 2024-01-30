import json
fp=open('data.json','r')
emp_data=json.load(fp)
#print(emp_data)

mcount=0

for user in emp_data:
    if user['gender']=='Male':
        mcount=mcount+1
        
print("No of male users:",mcount)

for user in emp_data:
    if user['gender']=='Male':
        print(user['name'],":",user['email'],"-",user['gender'])
        
fp.close()