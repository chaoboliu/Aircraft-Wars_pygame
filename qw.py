def q():
	import random
	a=random.randint(1,100)
	for i in range(1,20):
		r = int(input("请输入'99以内的数字'"))
		if r > a:
			print("恭喜中了一毛钱'继续抽奖请充值一元'")
			t = "****************"
			print(t.center(70,"*"))
		if r < a:
			print("恭喜中了一元钱'继续抽奖请充值一元'")
			t = "****************"
			print(t.center(70,"*"))
		elif r == a:
			print("恭喜中了一百元钱 '继续抽奖请充值一元'")
			t = "****************"
			print(t.center(70,"*"))
G = print("---------------------欢迎进入你充一元得一百元系统------------------")
v = int(input("请按1 进入系统"))
if v == 1:
	q()





















'''
def p():
	for i in range(1,20):
		r = int(input("请输入'99以内的数字'"))
		if r > a:
			print("一毛钱'继续抽奖请充值一元'")
'''






















