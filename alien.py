# -*- coding: gb2312 -*-
import pygame
from pygame.sprite import Sprite
from random import random
class Alien(Sprite):
	'''外星人类'''
	def __init__(self,screen,game_setting,x):
		super().__init__()
		self.screen=screen
		self.speed=game_setting.alien_speed_factor
		self.image=pygame.image.load('images/alien.bmp')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()
		self.rect.x = x
		self.rect.y = self.rect.height
		self.game_setting=game_setting
		self.y=float(self.rect.y)
		self.x=float(self.rect.x)
		self.flag=int(random()*3)
	def update(self):
		self.y+=self.speed
		self.rect.y=self.y
		if self.flag==1:
			self.x+=0.3
			if self.x>=1100:
				self.flag=2
		elif self.flag==2:
			self.x-=0.3
			if self.x<=100:
				self.flag=1
		self.rect.x=self.x
	def blitme(self):
		'''绘制外星人'''
		self.screen.blit(self.image,self.rect)
	
