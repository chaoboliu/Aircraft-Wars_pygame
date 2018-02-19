'''
name = "hello world what's your name?"
print(name)
name_bobo = "因为爱情"
print("因为爱情")
name_bobo = "我不爱你"
print("我不爱你")
print("那你爱谁")
name = "liu bochao."
print("\tMy name is %s"%name.title())
name = "Liu Bochao."
print("\tMy name is %s"%name.lower())
name = "liubochao."
print("\tMy name is %s"%name.upper())
first_name = "liu"
last_name = "bochao"
full_name = first_name + " " + last_name
print(full_name.title())
language = " python "
language = language.lstrip()
print(language)
a = 18.5
s = 2018+float(a)+3
print(s)

sex = ["小明","小红","小刚"]
print(sex[1]+":性别女")
print("我们班"+sex[1]+"是女孩!")
sex = ["小明","小红","小刚"]
print(sex[0],sex[2]+":性别男")
print("我们班"+sex[0],sex[2]+"是男孩!")




sex = ["小明","小红","小刚"]
print(sex)
sex[0]="小黄"
print(sex)

sex = ["校长"]
sex.append("小丽")
sex.append("狗蛋")
sex.append("豆豆")
sex.insert(1,"老师")
print(sex)


sex = ["小明","小红","小刚"]
sex.insert(1,"校长")
print(sex)


sex = ["小明","小红","小刚"]
print(sex)
del sex[0]
print(sex)


sex = ["小明","小红","小刚"]
print(sex)
sex.remove("小红")
print(sex)
'''
'''
print("放学啦！放学啦！校长和老师在和小明班长组织站排回家:\n 小刚，小红，狗蛋，豆豆")
print("-------------------------------------------------------------")
home = []
print("首先校长先上车 他负责驾驶并送我们回家")
home.append("校长")
print("校长上了车开着大汽车送俺们回家啦")
print(home)
print("**************************************************************")
print("之后小明带队，小刚小红狗蛋豆豆紧跟其后")
home.append("小明")
print(home)
home.append("小刚")
home.append("小红")
home.append("豆豆")
print(home)
print("***************************************************************")
print("狗蛋是同学里最后一个上的车，他说他有道题不会想去询问，并要挨着小明所以坐在小明的后面")
home.insert(2,"狗蛋")
print(home)
print("****************************************************************")
print("老师点完名之后随后上车关门")
home.insert(6,"老师")
print(home)
print("****************************************************************")
print("老师说：中间离下车门比较进所以我要坐到中间位置因为你们下车我得扶着你们下车，同学们说可以,于是老师坐在了小红的前面，老师的前面是小刚")
home.remove("老师")
home.insert(4,"老师")
print(home)
print("*****************************************************************")
print("就这么愉快的回家了，不一会儿，到了小刚家了，小刚说老师我要下车因为我到家了")
go_home = home.pop(3)
print(home)
print(go_home + "下车了 小刚说同学们老师们再见!")
print("老师说小刚回家好好写作业")
print("*******************************************************************")
print("不一会儿 豆豆也到家了")
go_home = home.pop(5)
print(home)
print("老师慢慢的扶着豆豆\t" + go_home +"说老师同学再见！")
print("*****************************************************************")
print("不一会儿，到了小明和小红家，小明和小红是龙凤胎所以他们是一家")
go_home = home.pop(1)
go_homes = home.pop(3)
print(home)
print("老师说你俩注意安全" + go_homes + go_home + "好的，异口同声说，小明班长说，明天狗蛋值日别忘记早去!")
'''
'''
zimu = []
zimu.append("d")
zimu.append("b")
zimu.append("c")
zimu.append("a")
zimu.sort()
print(zimu)
zimu.reverse()
print(len(zimu))
'''
'''
zimu = ["a","b","c"]
for zimus in zimu:
	print(zimus)
	print("下一个出场的是！")
print("欢迎大家")
'''
'''
list = []
a = input("请输入文字:")
list.append(a)
print(list)
for i in a:
	print(i,end="")
'''
'''
number = list(range(1,11,3))
print(number)
'''
'''
s = []
for value in range(1,11):
	l = value**2
	s.append(l)
print(s)
'''
'''
number = [1,2,5,8]
print(min(number))
print(max(number))
print(sum(number))
'''
'''
number = [value**2 for value in range(1,11)]
print(number)
'''
'''
zimu = ["a","b","c"]
print(zimu[0:2])
'''
'''
number = ["a","b","c","d","e"]
print(number[:1])
'''
'''
eat = ["羊肉串","板筋","骨肉相连"]
print(eat)
for lists in eat[0:1]:
	print(lists,end="")
'''
'''
my_friend_foods = ["羊肉串","板筋","骨肉相连"]
my_foods = my_friend_foods[0:2]
print("朋友爱吃的:",my_friend_foods)
print("我爱吃的:",my_foods)
my_foods.append("烤地瓜")
print("我又加了个：",my_foods[2:3])
for i in my_foods:
	print(i,end="")
'''
'''
car = ["bmw","cbb","qq"]
for cars in car:
	if cars == "bmw":
		print(cars.upper())
	else:
		print(cars.title())
'''
'''
a = {"color":"green","point":5}
print(a["color"])
print(a["point"])
'''
'''
a = {}
a["color"] = "green"
a["point"] = 5
print(a)
'''
'''
list = []
dic = {}
name = (input("请输入姓名:"))
tel = int(input("请输入电话:"))
dic["name"]=name
dic["tel"]=tel
list.append(dic)
print(list)
for i in list:
	for k,v in i.items():
		print("%s:%s"%(k,v))
'''
'''
dic = {}
dic["菜品"]="小葱拌豆腐"
dic["饮品"]="鸡蛋汤"
print(dic)
for k,v in dic.items():
	print("%s:%s"%(k,v))
'''
'''
list = []
dic = {}
name = input("请输入名字：")
tel = int(input("请输入电话号码："))
dic["name"]=name
dic["tel"]=tel
list.append(dic)
print(list)
for i in list:
	for k,v in i.items():
		print("%s:%s"%(k,v))
'''
'''
name = "继续请输入M,退出请输入Q \n 请输入内容:"
M = ""
while M != "Q":
	M = input(name)
	if M !="Q":
		print(M)
'''
'''
name = " a继续 q退出 \n"

a = True
while a:
	m = input(name)
	if m == "q":
		a = False
	else:
		print(m)
'''
'''
def a(b):
	print("hello!"+ b + "!")
a ("小明")
a ("小红")
a ("小兰")
'''
'''
def a():
	print("Hello!")
a()
a()
a()
'''
'''
def a(b,c):
	print("我家小狗叫:"+b+"!")
	print("你家小狗叫:"+c+"!")
	print(b+"真可爱!")
	print(c+"真可爱!")
a(c = "豆豆",b = "花花")
a(b = "月月",c = "兰兰")
a("宫本武藏","鲁班")
'''





















