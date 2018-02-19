class people():
	def __init__(self,name):
		self.__name = name
	def getGame(self):
		return self.__name
	def setName(self,newName):
		if len(newName) >= 5:
			self.__name = newName
		else:
			print("error:名字长度需要大于等于5")
xiaoming = People("xiaoming")
print(xiaoming.__name)

