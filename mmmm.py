
def print_narong():
	title="****"
	print(title.center(65,"*"))
	list=[]
	while True:	
		dic={}
		name = input("请输入名字")
		year = int(input("请输入年龄"))
		if not list:
			dic["name"]=name
			dic["year"]=year
			list.append(dic)
		else:
			cuo = False
			for i in list:
				for k,v in i.items():
					if v == name:
						print("您输入重复")
						cuo = True
						break

			if not cuo:
				dic["name"]=name
				dic["year"]=year
				list.append(dic)
		for i in list:
			for k,v in i.items():
				print(k,v)
print_narong()
