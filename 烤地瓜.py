class Digua:
	def __init__(self,name):
		self.name = name
	print("**********我的地瓜名**********")
	def printName(self):
		print("地瓜名字为:%s"%self.name)
def myPrint(Digua):
	Digua.printName()
s = Digua("辣酱地瓜")
myPrint(s)
p = Digua("变态辣地瓜")
myPrint(p)

class Digua:
	def __init__(self,typa):
		self.typa = typa
	print("*********地瓜种类**********")
	def printTypa(self):
		print("地瓜种类有:%s"%self.typa)
def myPrint(Digua):
	Digua.printTypa()
q = Digua("大的一块")
myPrint(q)
r = Digua("小的五毛")
myPrint(r)

class Diguaa:

	def __init__(self):
		self.cookedLever = 0
		self.cookedStr = "生的"
		self.condliments = []
	def cook(self,time):
		cookedStr = int(input("请输入① 键进行烘烤\n 请按键:"))
		self.cookedLever += time
		if self.cookedLever>8:
			self.cookedStr = "烤糊了"
		if self.cookedLever>5:
			self.cookedStr = "烤好了"
		if self.cookedLever>3:
			self.cookedStr = "中熟"
		else:
			self.cookedStr = "生的"
	def __str__(self):
		g = self.cookedStr+"地瓜"
		if len(self.condliments)>0:
			g = g + "("
			for temp in self.condliments:
				g = g + temp + ","
			g = g.strip(",")
			g = g + ")"
		return g
	def addcondiments(self,condliments):
		self.condliments.append(condliments)


myDiguaa = Diguaa()
print("----有了地瓜还没烤----")
print(myDiguaa.cookedLever)
#print(myDiguaa.cookedStr)
print(myDiguaa.condliments)

print("----接下来要进行烤地瓜了----")
print("----开始烤了----")
myDiguaa.cook(4)
print(myDiguaa)
myDiguaa.addcondiments("加番茄酱")
print("----地瓜又烤了5分钟----\n 请翻面\n")
myDiguaa.cook(3)
print(myDiguaa)
print("---接下来添加辣酱----")
myDiguaa.addcondiments("加辣酱")
print(myDiguaa)
print("----地瓜又烤了5分钟----")
print("烤好了 烤好了")

