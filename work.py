#作业第三题 带错误循环三次
myaccount = 88888
mypasswd = 88888
w = 0
c = 0
while w<3:
	account = int(input("请输入账号:"))
	passwd = int(input("请输入密码:"))
	if account == myaccount and passwd == mypasswd:
		print("欢迎来到 {我的世界}")
		break
	else:
		print("账号或密码错误")
	w+=1
else:
	print("稍后再试")


'''
		while c<1:
			print("稍后再试")
		c+=1
'''
