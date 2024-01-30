#convert json to dict
import json
emp_json='''{
    "eid":101,
    "ename":"Pavan",
    "esal": 45000,
    "avail":true,
    "discount":null
}'''

emp_dict=json.loads(emp_json)
print(emp_dict)
