#设一个类 "学生类"是抽象的
class Student():
#设一个函数 变量为hello (self)代表"学生"本身实例化 "self"是默认参数必须写 
	def hello(self):
#格式化打印 学生名字和年龄
		print("大家好，我是%s,我今年%d岁"%(self.name,self.age))
#实例 "学生"起名
	def setName(self,name):
		self.name = name
#实例 "学生"年龄
	def setAge(self,age):
		self.age = age
#实例化了一个学生
goudan = Student()
#调用实例函数 不需要手动输入self
goudan.setName("Goudan")
goudan.setAge(18)
goudan.hello()

maomao = Student()
maomao.setName("毛毛")
maomao.setAge(19)
maomao.hello()
