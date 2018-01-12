#第三题 带错误循环三次
'''
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

'''
		while c<1:
			print("稍后再试")
		c+=1
'''


#第一题
'''
for i in range (1,5001,1):
	if i%5 == 0 and i%7 == 0:
		print(i,end=" ")
'''	

#第二题
'''
import random
s = random.randint (1,100)
for i in range (1,11,1):
	r = int(input("请输入您的幸运数字"))
	if r>s:
		print("比%d小"%r)
	elif r<s:
		print("比%d大"%r)
	elif r==s:
		print("您猜对了大美女抱回家")
		break
'''
#第四题 用for 循环做的三角形
'''
for i in range (1,6,1):
	print("*"*i)
for a in range (4,0,-1):
	print("*"*a)
'''
# 用while 做第四题
'''
a = 1
while a <= 6:
	print("*"*a)
	a+=1
b = 5
while b > 0:
	print("*"*b)
	b-=1
'''



















