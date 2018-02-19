print("早餐我要去的店".center(45,"="))
class Restaurant(object):
	def __init__(self,restaurant_name,cuisine_type): #是属性
	
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type



	def describe_restaurant(self):
		print(self.restaurant_name)
		print(self.cuisine_type)
	def open_restaurant(self):
		print("饭店正常营业:")

restaurant1 = Restaurant("<<首都大饭店>>","鲍鱼龙虾，山珍海味，人参果 灵芝，各色海味好吃不贵。")
restaurant1.describe_restaurant()
restaurant1.open_restaurant()

restaurant2 = Restaurant("<<迪拜魔塔龙鬼屋饭店>>","宇宙飞船巧克力,变异魔鬼大龙虾，核岛辐射寿司。 \n 30元RMB 魔鬼自助")
restaurant2.describe_restaurant()
restaurant2.open_restaurant()

restaurant3 = Restaurant("<<太上老君龙子庄>>","废弃电池，地沟油，塑料瓶，酸雨，等蛋糕。 \n3元 RMB随便吃仅限今天")
restaurant3.describe_restaurant()
restaurant3.open_restaurant()

class User(object):
	def __init__(self,first_name,last_name,sex):
		self.first_name = first_name
		self.last_name = last_name
		self.sex = sex
	def describe_user(self):
		print(self.first_name)
		print(self.last_name)
		print(self.sex)
	def greet_user(self):
		print("年年年年")
user1 = User("刘","德华","真帅")
user1.describe_user()
user1.greet_user()














