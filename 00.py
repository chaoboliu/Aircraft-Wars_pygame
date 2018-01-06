'''
age = int(input("请输入年龄"))


if age < 18:
				print("不准谈恋爱")
elif age == 20:
   	print("抓紧找对象吧")
elif age > 30:
   	print("完了，单身狗")
else:
   	print("sorry,出错")
'''
'''
weizhi = input("请插入一个位置")


if weizhi == 'ADC':
    print("黄忠,后裔,虞姬")
if weizhi == '肉盾':
    print("亚瑟,程咬金")
if weizhi == '法师':
    print("王昭君,妲己")
if weizhi == '刺客':
    print("兰陵王,荆轲")
'''

#age = int(input("鲁班大还是亚瑟大?"))
       

'''

name = input("鲁班") 
oame = input("亚瑟")

if age  < 18:
    print("亚瑟:鲁班大")
else:
    print("鲁班大") 
'''

'''

sdcf = int(input("请您输入身高:"))
shenjia = int(input("请输入身价:"))
yzfen = int(input("请输入颜值分:"))


if sdcf >= 180 and shenjia > 1000000 and yzfen > 90:
    print("就可以是高富帅")
elif sdcf < 180 and shenjia > 100000 and yzfen > 90:
    print("就可以是富帅")
elif sdcf < 180 and shenjia < 1000000 and yzfen > 90:
    print("就可以是帅")
elif sdcf < 160 and shenjia < 100 and yzfen < 60:
    print("就可以是矮穷矬")

'''

'''
jisuanqi = int(input("在这里进行算题"))
x = 5  
y = 8
ghis = x+y
print(ghis)
ghis = x-y
print(ghis)
ghis = x*y
print(ghis)
g = x/y
print(g)
'''

'''

year = int(input("请在这里输入年份"))
if year %4 == 0 and year %100 !=0:
    print("闰年")
elif year %400 == 0: 
    print("是闰年")
else:
    print("平年")
'''



'''
h = float(input("请输入身高(m)"))
t = float(input("请输入体重(kg)"))
a = (t/(h*h))
print(a)
if a < 18.5:
    print("低于18.5 过轻")
elif a <= 26.2:
    print("低于25 正常")
elif a < 32:
    print("严重肥胖")
'''

'''
zhhh = input("请您输入账号:")

zh = '123456'
passwd = 'abc'


if zhhh == '123456':
    print("输入正确√")
else:
    print("×账号错误")

miaa = input("请您输入密码:")

if miaa == 'abc':
    print("登录成功√")
else:
    print("×登录失败稍后再试")

'''










'''
#登录银行账号密码

zhangh = int(input("请输入账号:"))
zh = 123456


if zhangh == zh:
    print("账号正确")
else:
    print("账号或密码错误")    

pwd = int(input("请输入密码:"))
mima = 123456


if pwd == mima:
    print("密码正确")
else:
    print("账号或密码错误")



if zhangh == zh and pwd == mima:
	
	model = int(input("请输入模式 存(1) 取(2)"))			
	if model == 1:
		#存钱流程
		cunkuan = int(input("请输入存款金额"))
		jine = 10000
		if cunkuan > 0:
			print("存钱金额为%d元存完后%d"%(cunkuan,cunkuan+jine))
	elif model == 2:
		#取钱流程 
		qmoney = int(input("请输入金额:"))
		jine = 10000
		if qmoney <= jine:
			print("取钱成功剩余%d元"%(jine-qmoney))
		else:
			print("金额不足取个毛线")
else:
	print("登录失败")
'''





 #头 剪刀 布

  

























































































