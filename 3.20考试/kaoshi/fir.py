# 使用pygame 我们先导入这个包
import pygame
from Plane_sprites import *
class PlaneGame(object):
# 飞机大战主游戏
	def __init__(self):
		print("游戏初始化")

		# 1. 创建游戏窗口 pygame.display.set_mode 创建游戏窗口 需要传宽和高 会给我们返回一个窗口
		# size 取宽高 x取x轴的值 y取y轴的值
		self.screen = pygame.display.set_mode(SCREEN_RECT.size)
		# 2.创建游戏时钟 pygame.time.Clock() 会给我们返回一个时钟对象
		self.Clock = pygame.time.Clock()
		# 3.调用私有方法 里面创建精灵和精灵组
		self.__create_sprites()
		# 4.设置定时器事件 每秒创建一架飞机
		pygame.time.set_timer(CREATE_ENEMY_EVENT,1000)
		# 5.每 0.5秒发射一个豆豆
		pygame.time.set_timer(HERO_FIRE_EVENT,500)
		pygame.time.set_timer(HEROO_FIRE_EVENT,500)
	
	def start_game(self):
		print("开始游戏")
		

		while True:
			# 1. 设置帧率
			self.clock.tick(60)
			# 2.事件监听
			self.__event_handler()
			# 3.碰撞检测
			self.__check_collide()
			# 4. 更新精灵组
			self.__update_sprites()
			# 5.更新屏幕显示
			pygame.display.update()

	def __create_sprites(self):
		# 创建精灵和精灵组
		# pygame.sprite.Group()可以创建一个精灵组
		# 1.背景 精灵组
		bg1 = Backgroup("./background.png")
		bg2 = Backgroup("./32ce7ee507daf21ea59f61dd10a430fe_meitu_1.png")
		bg2.rect.y = bg2.rect.height
		self.back_group = pygame.sprite.Group(bg1,bg2)
		# 2. 敌机精灵组 self.enemy_group = []
		self.enemy_group = pygame.sprite.Group()
		# 3. 英雄精灵组
		self.hero = Hero()
		self.hero_group = pygame.sprite.Group(self,hero)
		self.hero2 = Hero2()
		self.hero2_group = pygame.sprite.Group(self,hero2)
	
	def __event_handler(self):
		# 事件监听的方法
		# pygame.event.get() 获取监听事件列表
		# 获取列表以后 我写了一个for循环 循环这个列表
		for event in pygame enent.get():
			# 当前表里面有pygame.QUIT这个值 说明用户点了关闭按钮
			if event.type == pygame.QUIT:
			# 调用静态私有方法
				PlanGame.__game_over()
			elif event.type == CREATE_ENEMY_EVENT:
				enemy = Enemy()
				self.enemy_group.add(enemy)
			# 另外一个方案 返回所有按键的元祖 如果某个按键按下 对应值会是1
			Key_pressed = pygame.key.get_pressed()	
			if key_pressed = [pygame.K_SPACE]:
				self.hero2.fire2()
			if key_pressed[pygame.k_w]:
				self.hero.fire()
				
			
			if key_pressed[pygame.k_d]:
				print("向右移动")
				self.hero.speed = 2
			elif key_pressed[pygame.k_a]:
				self.hero.speed = -2
				print("向左移动")
			else:
				self.hero.speed = 0


			if key_pressed[pygame.K_RIGHT]:
				print("向右移动")
				self.hero2.speed = 2
			elif key_pressed[pygame.K_LEFT]:
				self.hero2.speed = -2
				print("向左移动")
			else:
				self.hero2.speed = 0



	def __check_collide(self):
		# 碰撞测试
		pygame.sprite.groupcollide(self.hero.bullets,self.enemy_group,True,True)
		pygame.sprite.groupcollide(self.hero2.bullets,self.enemy_group,True,True)
		enemies1 = pygame.sprite.spritecollide(self.hero,self.enemy_group,True) 
		enemies = pygame.sprite.spritecollide(self.hero2,self.enemy_group,True)
		if len(enemies1) > 0:
			self.hero.kill()
			PlaneGame.__game_over()
		if len(enemies) > 0:
			self.hero2.kill()
			PlaneGame.__game_over()
		
	def __update_sprites(self):
		# 更新精灵组
		for group in [self.back_group,self.enemy_group,self.hero_group,self.hero.bullets,self.hero2_group,self.hero2.bullets]:
			# 更新精灵组里面所有位置
			group.update()
			# 绘制到屏幕上
			group.draw(self.screen)
	
	@staticmethod
	def __game_over():
		# 游戏结束
		print("游戏结束")
		pygame.quit()
