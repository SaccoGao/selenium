username_1 = "sacco"
password_1 = 'Abcd1234'

print("请输入账号：")
username = input()

print("请输入密码：")
password = input()

if username == username_1:
    if password == password_1:
        print("登录成功！")
    else:
        print("密码错误！")
else:
    print("账号不存在！")