#read emp.json, print how many male users & female users.
import json
fp=open('emp.json','r')
data=json.load(fp)
print(data)

mcount=0
fcount=0
for user in data:
    if user['gender']=='Male':
        mcount=mcount+1
        
    if user['gender']=='Female':
        fcount=fcount+1
        
        
print("no of Male emp:", mcount)
print("no of Female emp:", fcount)
fp.close()