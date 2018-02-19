'''
def sum(a,b):
	def sum1(c):
		return a+b+c
	return sum1
result = sum(1,2)
name = result(10)
print(name)
'''

def calNum1(num):
	print(num)
	if num >1:
		return num*calNum1(num-1)
	else:
		print(num)
		return num
print(calNum1(5))
