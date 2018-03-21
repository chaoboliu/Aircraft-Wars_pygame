import pygame
import random
SCREEN_RECT = pygame.Rect(0,0,1101,600)
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
		image_name = "./dfvdf_2.png"
		super().__init__(image_name)
		if is_alt:
			self.rect.x = 1101

	def update(self):
		self.rect.x -= 4
		super().update()	
		if self.rect.x <= -1101:
			self.rect.x = 1101


class Hero(GameSprite):	
	def __init__(self):		
		super().__init__("./1.png")
		self.rect.centerx = SCREEN_RECT.centerx
		self.rect.bottom = SCREEN_RECT.bottom - 120

		self.bullets = pygame.sprite.Group()
		self.speed1 = 0
	def update(self):
		self.rect.x += self.speed
		self.rect.y += self.speed1
		if self.rect.y + self.rect.height <= 0: 
			self.rect.y = 50
		elif self.rect.y + self.rect.height >= 600:
			self.rect.y = 500
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

class Enemy(GameSprite):
	def __init__(self):
		super().__init__("./tu_4.png")
		self.speed = random.randint(5,8)
		self.rect.x = 1101
		max_y = SCREEN_RECT.height - self.rect.height
		self.rect.y = random.randint(self.rect.height,max_y)
	def update(self):
		self.rect.x -= self.speed
		if self.rect.right <= 0:
			#print("飞机飞出屏幕")
			self.kill()
	def __del__(self):
		pass
		#print("敌机被摧毁%s"%self.rect)
# 子弹类
class Bullet(GameSprite):
	def __init__(self):
		super().__init__("./3_meitu_6.png",20)
	def update(self):
		super().update()

		# 判断是否超出屏幕 如果是 从精灵组删除
		
		if self.rect.bottom < 0:
			self.kill()

class Eero(GameSprite):
	def __init__(self):
		super().__init__("./ccb0_meitu_2.png")
		self.rect.centerx = SCREEN_RECT.centerx
		self.rect.bottom = SCREEN_RECT.bottom - 200
		self.speed2 = 0
		self.bulletsa = pygame.sprite.Group()

	def update(self):
		self.rect.x += self.speed
		self.rect.y += self.speed2
		if self.rect.y + self.rect.height <= 0: 
			self.rect.y = 50
		elif self.rect.y + self.rect.height >= 700:
			self.rect.y = 500
		elif self.rect.left < 0:
			self.rect.left = 0
		elif self.rect.right > SCREEN_RECT.right:
			self.rect.right = SCREEN_RECT.right
	
	def fire(self):
		for i in range(1,4):
			self.bullet2 = Bullet2()
			# 设置精灵位置
			self.bullet2.rect.x = self.rect.x + 15*i + self.rect.width
			self.bullet2.rect.centery = self.rect.centery-20
			# 将精灵添加到精灵组
			self.bulletsa.add(self.bullet2)
class Bullet2(GameSprite):
	def __init__(self):
		super().__init__("./bullet1.png",10)
	def update(self):
		super().update()
	
		if self.rect.bottom < 0:
			self.kill()
