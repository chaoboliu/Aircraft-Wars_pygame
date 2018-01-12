'''
osum = 0
jsum = 0
zsum = 0
for i in range(0,101):
	if i%2 == 0:
		osum = osum+i
	if i%2 != 0:
		jsum = jsum+i
	zsum = zsum+i
print(osum)
print(jsum)
print(zsum)
'''
'''
a = {"wang":"1","liu":"2","zhang":"3"}
for i in a:
	print(i,a[i])
'''
'''
list = [{"name":"liubochao","age":12},{"name":"liuboyu","age":12},{"name":"zhaoyuan","age":12}]
for i in list:
	for j in i:
		print(j,i[j])
'''
'''
list = [{"na":1},{"ma":2}]
for i in list:
	for j in i:
		print(j,i[j])
'''
list = [["     *"],["    ***"],["   *****"],["  *******"],[" *********"],["***********"],["     *"],["    ***"],["   *****"],["  *******"],[" *********"],["***********"],["     *"],["    ***"],["   *****"],["  *******"],[" *********"    ],["***********"],["    **  "],["    **  "],["    **  "]]
for i in list:
	for j in i:
		print(j)

list = [{"beijing":{"mianji":1290,"remkou":123123},"shanghai":{"mianji":12331,"renkou":123123}}]
for i in list:
	for k,v in i.items():
		for b in v:
			print("%s   %s:%s"%(k,b,v[b]))





