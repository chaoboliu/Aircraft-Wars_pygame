'''
name = "苏三"
tel = 1234
dizhi = "地球"
print("name:%s tel:%d dizhi:%s"%(name,tel,dizhi))
'''



'''
for i in range(1,10):
	for j in range(1,i+1):
		print("%d*%d=%d"%(j,i,j*i),end= "\t")
	print("")
'''

year = int(input("请在这里输入年份"))
if year %4 == 0 and year %100 !=0 or year %400 == 0:
    print("闰年")
else:
    print("平年")

