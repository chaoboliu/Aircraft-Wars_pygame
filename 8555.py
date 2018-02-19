'''
s = "欢迎进入个人信息管理系统"
print(s.center(65,'*'))
list = []
while True:
	gongneng = int(input("请您选择功能：① 新增 ② 查询 ③ 修改 ④ 删除 请您进行选择:"))
	if gongneng == 1:
		name = input("请输入姓名")
		years =int(input("请输入年龄"))
		sex = input("请输入性别")
		work = input("请输入工作")
		list.append(name)
		list.append(years)	
		list.append(sex)
		list.append(work)
		print(list)
	elif gongneng == 2:
		g = int(input("请输入查询内容"))
		print(list[g])
'''

a = [["a","c"],["w","d"]]
for i in a:
	for j in i:
		print(j)


