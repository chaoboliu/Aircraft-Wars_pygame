def dd():
	for i in range(1,10):
		for a in range(1,i+1):
			print("%d*%d=%d"%(a,i,a*i),end="\t")
		print("")
def cc():
	print("                       oOoo ")
	print("                    o8888888o ")
	print("                     88 . 88 ")
	print("                    (| -_- |) ")
	print("                     O\\ = /O ")
	print("                 ____/`---'\\____ ")
	print("                . ' \\| |// `. ")
	print("                 / \\||| : |||// \\ ")
	print("               / _||||| -:- |||||- \\ ")
	print("                 | | \\\\\\ - /// | | ")
	print("               | \\_| ''\\---/'' | | ")
	print("                \\ .-\\__ `-` ___/-. / ")
	print("         ___    `. .' /--.--\\ `. . __ ")
	print("          ."" '< `.___\\_<|>_/___.' >'"". ")
	print("        | | : `- \\`.;`\\ _ /`;.`/ - ` : | | ")
	print("         \\ \\ `-. \\_ __\\ /__ _/ .-` / / ")
	print("  ======`-.____`-.___\\_____/___.-`____.-'====== ")
def zz():
	q = 0
	w = 0
	e = 0
	for i in range(1,101):
		if i%2 == 0:
				q += i
		elif i%2 !=0:
				w += i
		e += i
	print(q)
	print(w)
	print(e)


z = 0
x = 0
a = int(input("账号"))
b = int(input("密码"))
if z == a and x == b:
	print("正确")
	dd()
	cc()
	zz()
else:
	print("失败")

