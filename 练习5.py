# 一.设一个车类
class Car():
# 二.设初始化函数 放最前 括号后面的参数 首位必须self 然后跟后面的值
	def __init__(self,name,luntai,color,men):
# 三.传值
		self.name=name
		self.color=color
		self.luntai=luntai
		self.men=men
# 四.设魔法方法__str__ 他可以将变量abc里的值 用return打印出来  不用在实例化里写print步骤 所以是个不错的方法
	def __str__(self):
		abc="您好，车辆制造完毕"+"\n车名:"+self.name+ "车辆的颜色是："+self.color+",汽车轮子有"+str(self.luntai)+"个"+",车门数量"+str(self.men)+"个。"
		return abc
# 五.设dong函数变量 打印制造厂商
	def dong(self):
		print("制造厂商:阜新")


# ① .实例化 车型 设hanma为第一类里面的第一种车 （[二.① 两大块是紧密相连的]类里的值要和实例化的值相呼应 不能填错 luntai=10 color=黑色 men=10 ）
hanma = Car("悍马",10,"黑色",10)
print("开始制造 ... ...")
#开始格式化打印 颜色 轮胎 车门数量等和类相呼应内容
print("车的名字为:%s"%hanma.name)
print("车的颜色为:%s"%hanma.color)
print("车的轮胎为:%s个"%hanma.luntai)
print("车门数量为:%s个"%hanma.men)
# 设魔法方法id() 可以打印出"内存地址"
print("车的id为:",id(hanma))
hanma.dong()
print(hanma)

print("**************************************************************")

# ② . 实例化第二种车型 设mashaladi 为第一类的第二种车
mashaladi = Car("玛莎拉蒂",4,"极光蓝",2)
print("开始制造 ... ...")
print("车的名字为:%s"%mashaladi.name)
print("车的颜色为:%s"%mashaladi.color)
print("车门数量为:%s"%mashaladi.men)
print("车的轮胎为:%s"%mashaladi.luntai)
print("车的id为:",id(mashaladi))
mashaladi.dong()
print(mashaladi)
