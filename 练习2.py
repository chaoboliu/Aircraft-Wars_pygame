'''
def a(b,c):
	g = b+ " " +c
	return g.title()
s = a("l","e")
print(s)
'''
'''
def a(names):
	for name in names:
		g = "Hello!"+name.title()+"!"
		print(g)
s=["zhangfei","guanyu"]
a(s)
'''
'''
def a(ktvv):
	for ktv in ktvv:
		mv = "有请麦霸:"+" "+ktv+" "+"唱一首不同版青藏高原!"
		print(mv)
mtv=["刘欢","那英","毕福剑","迪克牛仔"]
a(mtv)
'''	

def a(f,l):
	n = f + " " + l
	return n.title()
while True:
	print("请输入您的英文(English)名字:\n 我们方便登记！\n按键.q.是退出键\n请在下方↓输入")
	print("******************************************************")
	f = input("您的姓:")
	if f=="q":
		break
	l = input("您的名:")
	if l == "q":
		break
	s = a(f,l)
	print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
	print("正在核对... ...\n您的姓为:"+f+"您的名为:"+l+"您的名字为:"+s)
	print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
