import requests

# get和post请求
requests.get('url', verify=False)
requests.post('url','data', verify=False)

# 解析请求
requests.get('url', verify=False).text # 把返回返回解析成功文本格式
requests.get('url', verify=False).json() # 把返回解析成Json格式
requests.post('url','data', verify=False).text # 把返回返回解析成功文本格式
requests.post('url','data', verify=False).json() # 把返回解析成Json格式

# 通过接口上传文件