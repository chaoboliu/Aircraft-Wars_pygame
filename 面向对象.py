# class是类
# 类具有 特征 和 行为
# 行为 代表方法
# 特征 代表属性

#面向对象和面向过程
# 面向对象 代表 例如 狗 吃 屎
# 面向过程 代表 例如 吃 狗 屎

# 创建一个类

class Dog:
	def _init_(self):  #当对象实例化的时候会自动执行
		self.name = "狗狗"
		self.age = 1
		self.hobby = "吃屎"
	def eat(self):

# 创建对象
	baby = Dog()
	print(f"姓名:{baby.name}")
	print(f"年龄:{baby.age}")
	print(f"爱好:{baby.hobby}")
	print(baby.eat())










		
