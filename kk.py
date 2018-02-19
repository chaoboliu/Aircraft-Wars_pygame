def q():
	list = []
	for i in range(2,101):
		a = True
		for a in range(2,i):
			if i%a == 0:
				a = False
				break
		if a:
			list.append(i)
	print(list)
print(result)
