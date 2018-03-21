import pygame
import random
SCREEN_RECT = pygame.Rect(0,0,1024,575)
CREATE_ENEMY_EVENT = pygame.USEREVENT
HERO_FIRE_EVENT = pygame.USEREVENT + 1

class GameSprite(pygame.sprite.Sprite):
	def __init__(self,image_name,speed=1):
		super().__init__()
		self.image = pygame.image.load(image_name)
		self.rect = self.image.get_rect()
		self.speed = speed

	def update(self,*args):
		self.rect.x += self.speed

class BackGround(GameSprite):
	def __init__(self,is_alt=False):
		image_name = "./efa_meitu_3.png"
		super().__init__(image_name)
		if is_alt:
			self.rect.x = 1024

	def update(self):
		self.rect.x -= 4
		super().update()	
		if self.rect.x <= -1024:
			self.rect.x = 1024


class Hero(GameSprite):	
	def __init__(self):		
		super().__init__("./itu_1_meitu_4.png")
		self.rect.centerx = SCREEN_RECT.centerx
		self.rect.bottom = SCREEN_RECT.bottom - 120

		self.bullets = pygame.sprite.Group()
		self.speed1 = 0
	def update(self):
		self.rect.x += self.speed
		self.rect.y += self.speed1
		if self.rect.y + self.rect.height <= 0: 
			self.rect.y = 40
		elif self.rect.y + self.rect.height >= 575:
			self.rect.y = 375
		elif self.rect.left < 0:
			self.rect.left = 0
		elif self.rect.right > SCREEN_RECT.right:
			self.rect.right = SCREEN_RECT.right

	def fire(self):

			for i in (0,1):
				self.bullet = Bullet()
				#设置精灵位置
				self.bullet.rect.x = self.rect.x + 15*i + self.rect.width
				self.bullet.rect.centery = self.rect.centery-20
				# 将精灵添加到精灵组
				self.bullets.add(self.bullet)
# 子弹类
class Bullet(GameSprite):
	def __init__(self):
		super().__init__("./3d_meitu_4.png",10)
	def update(self):
		super().update()

		# 判断是否超出屏幕 如果是 从精灵组删除
		
		if self.rect.bottom < 0:
			self.kill()




class Enemy(GameSprite):
	def __init__(self):
		super().__init__("./jkhkj7_meitu_2.png")
		self.speed = random.randint(7,10)
		self.rect.x = 1011
		max_y = SCREEN_RECT.height - self.rect.height
		self.rect.y = random.randint(0,max_y)
		self.bullets = pygame.sprite.Group()
	def update(self):
		self.rect.x -= self.speed
		if self.rect.right <= 0:
			print("飞机飞出屏幕")
			self.kill()
	def __del__(self):
		print("敌机被摧毁%s"%self.rect)

	
#	def fire(self):
#		for i in range(0,1):
#			self.bullet2 = Bullet2()
#			# 设置精灵位置
#			self.bullet2.rect.x = self.rect.x + 15*i + self.rect.width
#			self.bullet2.rect.centery = self.rect.centery-20
			# 将精灵添加到精灵组
#			self.bullets.add(self.bullet2)
#class Bullet2(GameSprite):
#	def __init__(self):
#		super().__init__("./3_meitu_6.png",-10)
#	def update(self):
#		super().update()
	
#		if self.rect.bottom < 0:
#			self.kill()
