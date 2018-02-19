'''
def sushu(b):
	list=[]
	for i in range(2,b):
		w = True
		for a in range(2,i):
			if i%a == 0:
				w = False
				break
		if w:
			list.append(i)
	print(list)

sushu(101)
'''
'''
#for 九九乘法表
for i in range(1,10):
	for a in range(1,i+1):
		print("%d*%d=%d"%(a,i,a*i),end="\t")
	print("")
'''
'''
#while 九九乘法表
count = 1
while count<10:
	a = 1
	while a < count+1:
		print("%d*%d=%d"%(a,count,a*count),end="\t")
		a+=1
	print("")
		
	count+=1
'''
def hanshu(a,b):
	oushu = 0
	jishu = 0
	sum = 0
	for i in range(a,b):
		if i%2 == 0:
			oushu+=i
		elif i%2 !=0:
			jishu+=i
	sum = oushu+jishu
	print(oushu,jishu,sum)
hanshu(1,101)
