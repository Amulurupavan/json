import json
fp=open('data.json','r')
data=json.load(fp)
print(data[0:50])

for user in data:
    print(user['email'][0:50])