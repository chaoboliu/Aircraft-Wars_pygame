#设一个学生类 类是抽象的 指的是学生这一大类
class Student():
    # 设初始化函数 __init__ 写法固定 在init前后都会有下划线  self必须作为第一个参数存在 然后在进行初始化值
	def __init__(self,name,age):
        #定义实例变量
		self.name = name
		self.age = age
    #设函数变量hello 并传值(self)这是一大类里的一种必须传self不然会报错 利用hello 调用打印出值
	def hello(self):
		print("大家好，我是%s,我今年%d岁"%(self.name,self.age))
#实例化 一个人物 Student进行实例化的时候，必须写入相应的参数 否则报错
maomao = Student("毛毛",21)
#调用函数hello 变量 并打印出相对应的参数值
maomao.hello()
zhangsan =Student("张三",20)
zhangsan.hello()
