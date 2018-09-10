# -*- coding: gb2312 -*-
import json
class  GameStats():
	def __init__(self,game_setting):
		self.filename='high_score'
		try:
			with open(self.filename) as f_obj:
				self.high_score=json.load(f_obj)
		except FileNotFoundError:
			self.high_score=0
			self.store_high_score()
		self.game_setting=game_setting
		self.reset_stats()
		self.game_active=False

			
	def store_high_score(self):
		with open(self.filename,'w') as f_obj:
			json.dump(self.high_score,f_obj)
			
	def reset_stats(self):
		self.store_high_score()
		self.ships_left = self.game_setting.ship_limit
		self.score=0
		self.level = 1

			
