#第一题两种方式不换横
'''
a = 1
while a<5001:
	if a%5 == 0 and a%7 == 0:
		print(a,end =" ")
	a+=1

for a in range (1,5001,1):
	if a%5 == 0 and a%7 == 0:
		print(a,end=" ")
'''
'''
import random
s = random.randint(1,100)
a = 1
while a<11:
	c = int(input("请输入数字"))
	if c > s:
		print("比%d小小小"%c)
	elif c < s:
		print("比%d大大大"%c)
	elif c == s:
		print("猜中了哈哈哈")
		break
	
	a+=1
'''
'''
a = 1
while a <= 5:
	print("*"*a)
	a+=1
s = 4 
while s > 0:
	print("*"*s)
	s-=1
'''
a = 10
while a > 0:
	print("*"*a)
	a-=1
'''
for i in range (1,10,1):
	for a in range (1,i+1,1):
		print("%d*%d=%d"%(a,i,a*i),end="\t")
	print("")
'''
'''
i = 1
while i < 10:
	a = 1
	while a <= i:
		print("%d*%d=%d"%(a,i,a*i),end="\t")
		a+=1
	print("")
	i+=1 
'''








