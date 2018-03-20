class LiuBochao(object):
	def aliubochao(self):
		import random
		a=random.randint(0,100)
		for i in range(1,20):
			r = int(input("请输入'99以内的数字'"))
			if r > a:
				print("猜大了")
				t = "****************"
				print(t.center(70,"*"))
			if r < a:
				print("猜小了")
				t = "****************"
				print(t.center(70,"*"))
			elif r == a:
				print("猜中了!!!!!!!!!!!!!!!!!!!!!!!!")
				break
				t = "****************"
				print(t.center(70,"*"))
wo = LiuBochao()
wo.aliubochao()
