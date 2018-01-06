

#石头 剪刀 步
#1.石头 2.剪刀 3.步

'''
import random
computer = random.randint(1,3)#电脑玩家

player = int(input("请输入 (1)石头(2)剪刀(3)布"))
if (player <= 3) and (player > 0):
	if (player == 1 and computer == 2) or (player == 2 and computer ==3) or(player == 3 and computer == 1):
		print("赢了")
	elif player == computer:
		print("平局")
	else:
		print("输了") 
		
else:
	print("输入不合法")
'''







'''
count = 0
mySum = 0 
while count < 100:
	if count !=0	
	print("当前数字:%d"%count)
	count+=1 
if mySum !==0	
	mySum =count + mySum
print("求和是%d"%mySum)
'''






'''

account = int(input("**************欢迎进入王者荣耀\n********************************************** 请输入账号: "))
zh = 123456


if account == zh:
	print("账号正确")
else:
	print("账号或密码错误")

passwd = int(input("(o-o)\n 请输入密码:"))

mi = 123456


if account == zh and passwd == mi:
	print("********************************正确 欢迎进入**************************")
else:
	print("账号和密码错误")

'''
'''

c = 1234
e = 1234

d = 0
while d<3:
	a = int(input("请输入账号"))
	b = int(input("请输入密码"))
	if a == c and b == e:
		print("登录成功")
		f = int(input("1 2 3 "))
		if f == 1:
			print("vv")
		elif g == 2:
			print("mm")
		elif h == 3:
			print("cc")
		break
	else:
		print("错误")
	d+=1
'''

'''
count = 1
while count <= 4:
	a = 1
	while a <= 4:
		print("o",end="")
		a +=1
	
	print("")
	count+=1
'''
'''

count = 1
while count <= 4:
	a = 1
	while a <= 8:
		print("口",end="")
		a +=1
	
	print("")
	count+=1
'''

'''
latiao = 1
money = 0
while latiao <= 10:
	jiage = 1
	while jiage <= 2:
		money = money+1
		jiage +=1

	latiao+=1
print("钱数为%d"%money)
''''



















