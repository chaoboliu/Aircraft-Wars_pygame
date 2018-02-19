for i in range(1,10):
	for a in range(1,i+1):
		print("%d*%d=%d"%(a,i,a*i),end="\t")
	print("")

count = 1
while count<10:
	a=1
	while a<count+1:
		print("%d*%d=%d"%(a,count,a*count),end="\t")
		a+=1
	print("")
	count+=1


name = "刘博超"
age = "20"
school = "北才"
tell = "15326245558"
print("name:%s,age:%s,tell:%s,school:%s"%(name,age,tell,school))

year = int(input("请输入年份"))
if year%4 == 0 and year%100 !=0 or year%400 == 0:
	print("是闰年")
else:
	print("是平年")
