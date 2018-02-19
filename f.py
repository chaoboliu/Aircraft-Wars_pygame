def adduser():
	name = input("请输入用户名字\n")
	age = input("请输入年龄\n")
	phone = input("请输入手机号\n")
	email = input("请输入邮箱\n")
	tel = input("请输入固定电话\n")
	company = input("请输入公司名称\n")
	position = input("请输入职位\n")
	remarks = input("请输入备注\n")
	isrepeat = False
	for dic in list :
		isrepeat = False
		if dic['名字'] == name:
			isrepeat = True	#判重
			print('用户已存在，请重新输入')
			break
	if not isrepeat :
		list.append({'名字':name,'年龄':age,'手机号':phone,'邮箱':email,'固定电话':tel,'公司':company,'职位':position,'备注':remarks})
		print("添加成功^_^\n")


#删除用户
def deluser():
	con = True
	while con:
		delname = input("请输入需要删除的用户\n")
		for dic in list:
			if dic['名字'] == delname:
				list.remove(dic)
				break
		print("删除成功")
		goon = int(input("继续修改请按１，结束请按０"))
		if goon == 0:
			con = False


#修改信息
def change():
	con = True
	while con:
		change_Name = input("请输入要修改的用户\n")
		option = int(input("请输入要修改的信息 (1)年龄,(2)手机号,(3)邮箱,(4)固定电话,(5)公司,(6)职位,(7)备注\n"))
		change = input("修改为:\n") 
		list_Option=[0,'年龄','手机号','邮箱','固定电话','公司','职位','备注']
		for dic in list:
			for k in dic:
				if k == list_Option[option]: 
					dic[k] = change
		print("修改成功")
		print(list)
		goon = int(input("继续修改请按１，结束请按０"))
		if goon == 0:
			con = False


#查询
def find():
	con = True	
	while con:
		find_Name = input("请输入你查询的用户名")	
		for dic in list :
			if dic['名字']==find_Name:
				print(dic)		
		goon = int(input("继续查询请按１，结束请按０"))
		if goon == 0:
			con = False


#名片信息管理系统
Title = "名片信息管理系统"
print(Title.center(70,'*'))
list = []
while True :
	fn=input("功能:(1)添加名片,(2)删除名片，(3)修改名片,(4)查询名片,(5)退出系统\n")
	if fn == '1':
		adduser()
	if fn == '2':
		deluser()
	if fn == '3':
		change()
	if fn == '4':
		find()
	if fn == '5':
		break
	else :
		print("")
	print(list)
	print(70*'*')
	

