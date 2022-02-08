import json

student = [
    {'name':'Sacco1', 'age':18, 'flag':False},
    {'name':'Sacco2', 'age':18}
          ]

Json_str = json.dumps(student)
print(type(Json_str))
print(Json_str)