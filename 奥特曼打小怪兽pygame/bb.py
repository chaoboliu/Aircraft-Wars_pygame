# 导入pygame模块:
import pygame 
from cc import *
pygame.init()
pygame.mixer.music.load("./儿童歌曲-黑猫警长1.mp3")
pygame.mixer.music.play()


class PlaneGame(object):
	def __init__(self):
		self.screen = pygame.display.set_mode((SCREEN_RECT.width,SCREEN_RECT.height))
		self.clock = pygame.time.Clock()
		self.__create_sprites()
		pygame.time.set_timer(CREATE_ENEMY_EVENT,300)
		pygame.time.set_timer(HERO_FIRE_EVENT,1000)
		#self.mama = False		



	def start_game(self):
		print("开始游戏")
		while True:
			self.clock.tick(60)
			self.name = pygame.display.set_caption("无敌奥特曼")
			self.__handler_event()
			self.__check_collide()
			self.__update_sprites()
			pygame.display.update()

	def __create_sprites(self):
		self.hero = Hero()
		self.hero_group = pygame.sprite.Group(self.hero)
		#self.eero = Eero()
		#self.eero_group = pygame.sprite.Group(self.eero)
		self.enemy = Enemy()
		self.enemy_group = pygame.sprite.Group(self.enemy)
		bg1 = BackGround()
		bg2 = BackGround(True)
		self.back_group = pygame.sprite.Group(bg1,bg2)

	def __handler_event(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				exit()
			elif event.type == CREATE_ENEMY_EVENT:
				new_enemy = Enemy()
				self.enemy_group.add(new_enemy)
				#print("敌机出场....")

			elif event.type == HERO_FIRE_EVENT:
				self.hero.fire()
				#self.enemy.fire()

			keys_pressed = pygame.key.get_pressed()
			if keys_pressed[pygame.K_RIGHT]:
				self.hero.speed = 8
			elif keys_pressed[pygame.K_LEFT]:
				self.hero.speed = -8
			elif keys_pressed[pygame.K_UP]:
				self.hero.speed1 = -8
			elif keys_pressed[pygame.K_DOWN]:
				self.hero.speed1 = 8
			#elif keys_pressed[pygame.K_SPACE]:
				#self.hero.fire()
			else:
				self.hero.speed = 0
				self.hero.speed1= 0
			#keys_pressed = pygame.key.get_pressed()
			#if keys_pressed[pygame.K_d]:
			#	self.eero.speed = 8
			#elif keys_pressed[pygame.K_a]:
			#	self.eero.speed = -8
			#elif keys_pressed[pygame.K_w]:
			#	self.eero.speed2 = -8
			#elif keys_pressed[pygame.K_s]:
			#	self.eero.speed2 = 8
			#elif keys_pressed[pygame.K_q]:
				#self.eero.fire()
		#	else:
		#		self.eero.speed = 0
		#		self.eero.speed2= 0




				
				
	def __check_collide(self):
		pygame.sprite.groupcollide(self.hero.bullets,self.enemy_group,True,True)
		#pygame.sprite.groupcollide(self.enemy.bullets,self.enemy_group,True,True)
		enemies = pygame.sprite.spritecollide(self.hero,self.enemy_group,True)
		#enemies2 = pygame.sprite.spritecollide(self.enemy,self.enemy_group,True)

		if len(enemies) > 0:
				self.hero.kill()
				PlaneGame.__game_over()
	def __update_sprites(self):
		#1 更新位置 2绘制
		self.back_group.update()
		self.back_group.draw(self.screen)
		self.hero_group.update()
		self.hero_group.draw(self.screen)
		#self.eero_group.update()
		#self.eero_group.draw(self.screen)
		self.enemy_group.update()
		self.enemy_group.draw(self.screen)
		self.hero.bullets.update()
		self.hero.bullets.draw(self.screen)
		self.enemy.bullets.update()
		self.enemy.bullets.draw(self.screen)
		#self.eero.bulletsa.update()
		#self.eero.bulletsa.draw(self.screen)

	def __game_over():	
		print("游戏结束")
		pygame.quit()
		exit()
if __name__ == "__main__":
	#使用游戏类 创建一个游戏对象
	game = PlaneGame()
	#开始游戏
	game.start_game()



