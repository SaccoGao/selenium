# 反序列化：把字符串转化为内置的数据类型
import json

# 接收到的Json字符串为对象
json_str_1 = '{"name":"Sacco", "age":18}'

student1 = json.loads(json_str_1)  # 把Json转化为字典Dict
print(student1)

# 接收到的为多个Json对象组成的数组
json_str_2 = '[{"name":"Sacco1", "age":18},{"name":"Sacco2", "age":18}]'

student2 = json.loads(json_str_2)  # 把Json转化为列表list,列表内的元素为字典Dict
print(student2)

