# -*- coding: utf-8 -*-
"""
Created on Tue Jun 22 17:25:27 2021

@author: ali_d
"""
# Json
import json


person_string = '{"name":"ali","languages":["python","C#"]}'
# result = person["name"]
# print(result)
# result = person["languages"]
# print(result)


#Json string to Dict

result = json.loads(person_string)
print(result)
print(type(result))

# result = result["name"]
# print(result)
# result["languages"]
# print(result

#%%
with open("json.json") as f:
    data=json.load(f)
    print(data["name"])
    print(data["languages"])
    print(data)    


#%%

person_dict = {
    "name":"ali",
    "languages":["python","c#"]
    }

#Dict to Json string
result = json.dumps(person_dict)
print(result)
#print(result["name"])
print(type(result))

#%%
with open("json2.json","w") as f:
    json.dump(person_dict,f)
    
    
#%%
person_string = '{"name":"ali","languages":["python","C#"]}'

person_dict = json.loads(person_string )
result = json.dumps(person_dict,indent=4,sort_keys=True)
print(person_dict)
print()
print(result)



#%% 



































































































