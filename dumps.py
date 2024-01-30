# convert dict to json 
import json
emp_dict={
    'eid':101,
    'ename':'Pavan',
    'esal': 45000.00,
    'avail':True,
    'discount':None
}

emp_json=json.dumps(emp_dict)
print(emp_json)
