distance = float(input("请输入距离"))

money = 0
sum = 0
for i in range(0,60):
	if distance <= 6:
		money = 3
	elif 6 < distance  and distance <= 12:
		money = 4
	elif 12 < distance and distance <= 22:
		money = 5
	elif 22 < distance and distance <= 32:
		money = 6
	elif distance > 32:
		if (distance-32)%20 == 0:
			money = 6 + (distance -32) /20 
		else:
			money = 6 + int((distance - 32) /20)+1		
	if sum >=100  and sum < 150:
		money = money *0.8
	elif sum >= 150 and sum < 400:
		money = money * 0.5

	sum +=money
print("一共花了%.2f"%sum)	
