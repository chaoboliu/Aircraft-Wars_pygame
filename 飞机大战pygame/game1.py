# 导入pygame模块:
import pygame 
from z import *
pygame.init()
pygame.mixer.music.load("./7爷-撒贝宁杀乌鸡 - 铃声.mp3")
pygame.mixer.music.play()


class PlaneGame(object):
	def __init__(self):
		self.screen = pygame.display.set_mode((SCREEN_RECT.width,SCREEN_RECT.height))
		self.clock = pygame.time.Clock()
		self.__create_sprites()
		pygame.time.set_timer(CREATE_ENEMY_EVENT,800)
		pygame.time.set_timer(HERO_FIRE_EVENT,300)
		self.ji_fen = 0


	def start_game(self):
		print("开始游戏")
		while True:
			self.clock.tick(60)
			self.name = pygame.display.set_caption("飞机大战")
			self.__handler_event()
			self.__check_collide()
			self.__update_sprites()
			self.__print_score()
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
				print("敌机出场....")




			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RIGHT:
					self.hero.moving_right = True
				elif event.key == pygame.K_LEFT:
					self.hero.moving_left = True
				elif event.key == pygame.K_UP:
					self.hero.moving_up = True
				elif event.key == pygame.K_DOWN:
					self.hero.moving_down = True

			elif event.type == pygame.KEYUP:
				if event.key == pygame.K_RIGHT:
					self.hero.moving_right = False
				elif event.key == pygame.K_LEFT:
					self.hero.moving_left = False
				elif event.key == pygame.K_UP:
					self.hero.moving_up = False
				elif event.key == pygame.K_DOWN:
					self.hero.moving_down = False
			elif event.type == HERO_FIRE_EVENT:
				self.hero.fire()

				

				
				
	def __check_collide(self):
		if pygame.sprite.groupcollide(self.hero.bullets,self.enemy_group,True,True):
			self.ji_fen+=1
		enemies = pygame.sprite.spritecollide(self.hero,self.enemy_group,True)
			
		if len(enemies) >0:
			self.hero.kill()
			PlaneGame.__game_over()	

	def __print_score(self):
		pygame.font.init()
		pos1 = (200,0)
		color = (255,192,203)
		text1 = "  "+str(self.ji_fen)
		cur_font = pygame.font.SysFont("粗体",80)
		text_font1 = cur_font.render(text1,1,color)
		self.screen.blit(text_font1,pos1)

	def __update_sprites(self):
		#1 更新位置 2绘制
		self.back_group.update()
		self.back_group.draw(self.screen)
		self.hero_group.update()
		self.hero_group.draw(self.screen)
		#elf.eero_group.update()
		#self.eero_group.draw(self.screen)
		self.enemy_group.update()
		self.enemy_group.draw(self.screen)
		self.hero.bullets.update()
		self.hero.bullets.draw(self.screen)

	def __game_over():	
		print("游戏结束")
		pygame.quit()
		exit()
	
if __name__ == "__main__":
	#使用游戏类 创建一个游戏对象
	game = PlaneGame()
	#开始游戏
	game.start_game()


