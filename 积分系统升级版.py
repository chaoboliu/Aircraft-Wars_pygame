list = []
dic = {}
def aa():	
		name = input("请输入姓名:")	
		year = int(input("请输入年龄:"))
		sex = input("请输入性别:")
		jifen = int(input("请输入积分余额:"))
		dic["name"]=name
		dic["year"]=year
		dic["sex"]=sex
		dic["jifen"]=jifen
		list.append(dic)
		print(list)
		for i in list:
			for k,v in i.items():
				print("%s:%s"%(k,v))
def	bb():
		soso = input("请输入您要查询的名字:")
		for dic in list:
			if soso == dic["name"]:
				print("名字:%s 积分:%d"%(dic["name"],dic["jifen"]))
def cc():
		name = input("请输入您要修改的名字:")
		for dic in list:
			if dic["name"] == name:
				name2 = input("请输入您要替换的新名字:")
				dic["name"] = name2
				guanli = int(input("由于网络缓冲 '请按2号键 查询修改成功' 欢迎您来到功能管理系统：\n请选择功能:① 新增 ② 查询 ③ 修改 ④ 删除 ⑤ 退出 "))
				soso = input("请输入您要查询的名字:")
				for dic in list:
					if soso == dic["name"]:
						print("名字:%s 积分:%d"%(dic["name"],dic["jifen"]))

def dd():
		name = input("请输入您要删除的名字:")
		sp = 0
		for dic in list:
			if dic["name"] == name:
				del list[sp]
			else:
				sp+=1
			guanli = int(input("由于网络缓冲 '删除成功 请按2号键 确认成功' 欢迎您来到功能管理系统：\n请选择功能:① 新增 ② 查询 ③ 修改 ④ 删除 ⑤ 退出 "))
			soso = input("请输入您要查询的名字:")
			for dic in list:
				if soso == dic["name"]:
					print("名字:%s 积分:%d"%(dic["name"],dic["jifen"]))
					print("删除成功☺")
def ee():
		print("退出")


title = "欢迎进入 会员积分 管理系统"
print(title.center(65,"*"))
z = 666666
m = 666666
account = int(input("请输入管理系统账号："))
passwd = int(input("请输入管理系统密码："))
if account == z and passwd == m:
	print("账号密码登录成功，欢迎进入系统！")
	print("----------------------------------------------------------------------------")
	while True:
		guanli = int(input("欢迎您来到功能管理系统：\n请选择功能:① 新增 ② 查询 ③ 修改 ④ 删除 ⑤ 退出 "))
		if guanli == 1:
			aa()
			t = "****************"
			print(t.center(70,"*"))
		if guanli == 2:
			bb()
			t = "****************"
			print(t.center(70,"*"))
		if guanli == 3:
			cc()
			t = "****************"
			print(t.center(70,"*"))
		if guanli == 4:
			dd()
			t = "****************"
			print(t.center(70,"*"))
		if guanli == 5:
			ee()
			t = "****************"
			print(t.center(70,"*"))
			break
	print("※ ※ ※ ※ ※ ※ ※ ※ ※ ※ ※ ※ ※ ※ ※ ※ ※ ※ ※ ※ ※ ※ ※ ※ ※ ※ ※ ※ ※ ※ ※ ※ ※ ※ ※ ※ ※ ※ ※ ")
else:
	print("账号或密码错误")







			

	
				
