# -*- coding: gb2312 -*-
import pygame
from pygame.sprite import Sprite
class Bullet(Sprite):
	'''子弹类'''
	def __init__(self,screen,ship,game_setting):
		super().__init__()
		self.screen=screen
		
		self.rect=pygame.Rect(0, 0, 5,15)
		self.rect.centerx=ship.rect.centerx
		self.rect.top=ship.rect.top
		
		self.color = game_setting.bullet_color
		self.speed = game_setting.bullet_speed_factor
		
	def update(self):
		self.rect.y-=self.speed
		
	def blitme(self):
		pygame.draw.rect(self.screen, self.color, self.rect)
	
