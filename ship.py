# -*- coding: gb2312 -*-
import pygame
from pygame.sprite import Sprite
import time
class Ship(Sprite):
	'''初始化飞船并设置其初始值'''
	def __init__(self, screen,game_setting):
		super().__init__()
		self.screen=screen
		self.speed=game_setting.ship_speed_factor
		self.image=pygame.image.load('images/ship.bmp')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()
		self.left_flag=False
		self.right_flag=False
		'''设置飞船位置'''
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom
		self.time_begin=time.time()
		self.time_end=time.time()
	def update(self):
		if self.left_flag and self.rect.left > 0:
			self.rect.centerx -= self.speed
		if self.right_flag and self.rect.right < self.screen_rect.right:
			self.rect.centerx += self.speed
		
	def blitme(self):
		'''绘制飞船'''
		self.screen.blit(self.image,self.rect)
