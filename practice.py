q = 123
w = 123
e = 0
while e<3:
	a = int(input("输入账号："))
	s = int(input("输入密码："))
	if a == q and s == w:
		print("密码正确")
		v = int(input("1存钱 2取钱 3查看余额"))
		if v == 1:
			money = 100	
			cunqian = int(input("请输入存钱金额："))
			if cunqian > 0:	
				print("存款金额为%d元 剩余金额为%d元"%(cunqian,cunqian+money))
		elif v == 2:
			money = 100
			quqian = int(input("请输入取钱金额:"))
			if quqian <= money:	
				print("当前金额为%d元 剩余金额为%d元"%(quqian,money-quqian))
		elif v == 3:
			money = 100
			print("当前金额为%d元"%money)
		break
	else:
		print("账号或密码错误")
	e+=1
else:
	print("由于您账号密码次数过多 请明日再试")







