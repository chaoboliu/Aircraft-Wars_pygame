# 选区类
print("❤"*78)
class Xuanqu(object):
    # 类 属性 通过它可以满足条件(不满足条件为假)
	is_login = False
	def denglu(self):
		print("欢迎进入CS游戏选区界面\t 请您选区:\t电信A区 \t网通B区")
		print("❤"*78)
		A = input("请输入区域(A)或(B)进入游戏:")
		if A == A or A == B:
			print("欢迎进入登录界面")
			print("❤"*78)
	def zhang(self):
		count = 1
		while count <= 3:
			print("请登录账号和密码")
			D = input("请输入账号:")
			M = input("请输入密码:")
			if D == "12" and M == "12":
				print("登录成功!")
				# 满足登录条件 为真 就可以 (进行下一类)
				Xuanqu.is_login = True
				break
			else:
				print("账号或密码错误")
			count += 1
		
# 人类
print("❤"*78)
class Person(object):
	def people(self):
		print("❤"*78)
		print("《《开始创建人物》》 ")
		print("请选择角色属性:\n <角色① :白狼 性别：男 武器：AK47黑武士 手枪：暗杀者 近身武器：马来剑> \n <角色② :黑锋 性别：男 武器：M4A1死神 手枪：牡丹 近身武器：龙啸>\n<角色③ :夜玫瑰 性别：女 武器：AK47 手枪：修罗 近身武器：尼泊尔>\n <角色④ :潘多拉 性别：女 武器：巴雷特  手枪：牡丹 近身武器：玫瑰手斧>\n(其他角色敬请期待)")
		print("❤"*78)
		A = input("请(选择)角色:")
		if "1" == A:
			print("创建角色成功!\t白狼 性别：男 武器：AK47黑武士 手枪：暗者 近身武器：马来剑")
		if "2" == A:
			print("创建角色成功!\t黑锋 性别：男 武器：M4A1死神 手枪：牡丹 近身武器：龙啸")
		if "3" == A:
			print("创建角色成功!\t夜玫瑰 性别：女 武器：AK47 手枪：修罗 近身武器:尼泊尔")
		if "4" == A:
			print("创建角色成功!\t潘多拉 性别：女 武器：巴雷特  手枪：牡丹 近身武器：玫瑰手斧")
		print("❤"*78)



	def wing(self):
		import random
		A=input("请选择:按① 可以查看随机您喜欢创建的名字 并查看,按② 继续输入:")
		if "1" == A:
			for i in range(1,4):
				list = ["孤独求败","大鱼小鱼","齐天大圣","令狐者","你的皇帝在此","我爱Python","猫和老鼠","淘气三千问","米老鼠唐老鸭"]
				my_random = random.randint(0,len(list))
				print("系统为您随机选择:",list[my_random-1],"\t温馨提示:喜欢输入,不喜欢自己想!")
	print("❤"*78)
	def ming(self):
		list = []
		dic = {}		
		name = input("请创建姓名:")
		age = int(input("请创建年龄:"))
		print("❤"*78)
		dic["名称"]=name
		dic["年龄"]=age
		list.append(dic)
		#print(list)
		for i in list:
			for k,v in i.items():
				print("%s:%s"%(k,v))
	def shangcheng(self):
		print("❤"*78)
		k = 1000
		print("您现有金额%d;请合理安排您的资金,祝您游戏愉快!"%k)
		print("❤"*78)
		A = input("《欢迎进入商城》\n【子弹系列】\n请购买您需要的子弹:① 高级子弹:300元,② 中级子弹:200元,③ 低级子弹:100元\n请选择:")
		if "1" == A:
			a = k - 300
			k = a
			print("您成功购买高级子弹100发!花掉300元剩余%d元"%k)
		if "2" == A:
			b = k - 200
			k = b
			print("您成功购买中级子弹100发!花掉200元剩余%d元"%k)
		if "3" == A:
			c = k - 100
			k = c
			print("您成功购买初级子弹100发!花掉100元剩余%d元"%k)
	# 枪
			print("❤"*78)
		A = input("【手枪系列】\n请购买您需要的手枪:① 高级手枪:200元,② 中级手枪:100元,③ 低级手枪:80元\n请选择:")
		if "1" == A:
			a = k - 200
			k = a
			print("您成功购买高级手枪!花掉200元剩余%d元"%k)
		if "2" == A:
			b = k - 100
			k = b
			print("您成功购买中级手枪!花掉100元剩余%d元"%k)
		if "3" == A:
			c = k - 80
			k = c
			print("您成功购买初级手枪!花掉80元剩余%s元"%k)
		A = input("【装备系列】\n请购买您需要的手枪:① 高级装备:300元,② 中级装备:200元,③ 低级装备:100元\n请选择:")
		if "1" == A:
			a = k - 300
			k = a
			print("您成功购买高级装备!花掉300元剩余%d元"%k)
		if "2" == A:
			b = k - 200
			k = b
			print("您成功购买中级装备!花掉200元剩余%d元"%k)
		if "3" == A:
			c = k - 100
			k = c
			print("您成功购买初级装备!花掉100元剩余%s元"%k)
			print("❤"*78)


# 上战场
class Zhanchang(object):
# 一共大战四回 三回运气 终极大招 猜古诗
	def cai(self):
		q = input("《欢迎进入游戏》按1 进入 [排位赛]:")
		if "1" == q:
			print("杀呀!!! 杀呀!!! 敌人来了!! 拿起我们的装备上战场啦! 注意危险!! 危险!!")
			print("-"*78)
		w = input("我们已经来到了[敌方轰炸区] 装上我们的定时炸药!!《输入炸药密码:111》:")
		if "111" == w:
			print("咣!!!! 咣!!! ")
			print("-"*78)


		import random
		a = random.randint(1,11)
		for i in range(1,4):
			R = int(input("请您去 敌区 输入您的幸运(1-10)的数字 并轰炸区域:"))
			if R > a:
				print("炸死一百人")
				t = "****************"
				print(t.center(70,"*"))
			if R < a:
				print("炸死二百人")
				t = "****************"
				print(t.center(70,"*"))
			elif R == a:
				print("炸死五百人")
				t = "****************"
				print(t.center(70,"*"))
		print("《敌人说:要吟诗一首》 如果你能接上,我们认输!")
		import random
		for i in range(1,4):
			list = ["春眠不觉晓,","锄禾日当午,","飞流直下三千尺,","唧唧复唧唧","坐车停爱枫林晚"]
			sy_random = random.randint(0,len(list))
			print("你对吧!:",list[sy_random-1])
			if sy_random == 1:
				Z = input("请对诗:\nA,一二山四五\nB,上山打老虎\nC,老虎没大招\nD,一枝红杏出墙来\nE,疑是银河落九天\nF,汗滴禾下土\nH,处处闻啼鸟\nI,木兰当户织\nJ,我爱你爱着你就像老鼠爱大米\n请选择诗句的下一句:" )
				if Z == "H":
					print("您输入的正确")
					print("❤"*78)
				else:
					print("您输入的错误")
					print("-"*78)
			if sy_random == 2:
				Z = input("请对诗:\nA,一二山四五\nB,上山打老虎\nC,老虎没大招\nD,一枝红杏出墙来\nE,疑是银河落九天\nF,汗滴禾下土\nH,处处闻啼鸟\nI,木兰当户织\nJ,我爱你爱着你就像老鼠爱大米\n请选择诗句的下一句:" )
				if Z == "F":
					print("《您输入的正确》")
					print("❤"*78)
				else:
					print("×您输入的错误×")
					print("-"*78)
			if sy_random == 3:
				Z = input("请对诗:\nA,一二山四五\nB,上山打老虎\nC,老虎没大招\nD,一枝红杏出墙来\nE,疑是银河落九天\nF,汗滴禾下土\nH,处处闻啼鸟\nI,木兰当户织\nJ,我爱你爱着你就像老鼠爱大米\n请选择诗句的下一句:" )
				if Z == "E":
					print("《您输入的正确》")
					print("❤"*78)
				else:
					print("×您输入的错误×")
					print("-"*78)
			if sy_random == 4:
				Z = input("请对诗:\nA,一二山四五\nB,上山打老虎\nC,老虎没大招\nD,一枝红杏出墙来\nE,疑是银河落九天\nF,汗滴禾下土\nH,处处闻啼鸟\nI,木兰当户织\nJ,我爱你爱着你就像老鼠爱大米\n请选择诗句的下一句:" )
				if Z == "I":
					print("《您输入的正确》")
					print("❤"*78)
				else:
					print("×您输入的错误×")
					print("-"*78)
			if sy_random == 5:
				Z = input("请对诗:\nA,一二山四五\nB,上山打老虎\nC,老虎没大招\nD,一枝红杏出墙来\nE,疑是银河落九天\nF,汗滴禾下土\nH,处处闻啼鸟\nI,木兰当户织\nJ,我爱你爱着你就像老鼠爱大米\n请选择诗句的下一句:" )
				if Z == "D":
					print("《您输入的正确》")
					print("❤"*78)
				else:
					print("×您输入的错误×")
					print("-"*78)

# 战绩结果
class Zhanji(object):
	def jieguo(self):
		print("您赢了!!! 我们送您一个大礼")
		import random
		a=random.randint(1,11)
		for i in range(1,2):
			r = int(input("请您输入(1~10)选择礼包,谢谢体验!"))
			if r > a:
				print("让梦想飞在窗外,去迎接那未知的精彩!")
				t = "****************"
				print(t.center(70,"*"))
			if r < a:
				print("只有经历过地狱般的磨炼,才能拥有征服天堂的力量,只有流过血的手指,才能弹出世间的绝响!")
				t = "****************"
				print(t.center(70,"*"))
			elif r == a:
				print("立志欲坚不欲锐,成功在久不在速.")
				t = "****************"
				print(t.center(70,"*"))


 #实例 选取区类和 人物类
adenglu = Xuanqu()
renwu = Person()
wo = Zhanchang()
me = Zhanji()
adenglu.denglu()
adenglu.zhang()
if Xuanqu.is_login:
	renwu.people()
	renwu.wing()
	renwu.ming()
	print("游戏账号:",id(renwu))
	renwu.shangcheng()
	wo.cai()
	me.jieguo()
