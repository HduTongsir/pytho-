# -*- coding: gb2312 -*-
import pygame
import sys
from setting import Settings
from ship import Ship
from alien import Alien
from total import GameStats
from score import Scoreboard
from game_function import check_event
from game_function import update_screen
from pygame.sprite import Group
from random import random
from button import Button
from time import sleep
def run_game():
	game_setting=Settings()
	pygame.init()
	screen = pygame.display.set_mode((game_setting.screen_width, game_setting.screen_height))
	pygame.display.set_caption(game_setting.caption)
	stats = GameStats(game_setting)	
	score = Scoreboard(game_setting, screen, stats)
	ship=Ship(screen,game_setting)
	play_button=Button(game_setting,screen,"play")
	bullets = Group()
	big_bullets=Group()
	aliens = Group()
	count=0
	tim=500	
	screen.fill(game_setting.bg_color)#填充颜色
	pygame.display.flip()
	#游戏循环开始
	while True:
		count+=1
		check_event(game_setting,ship,bullets,screen,play_button,stats,score,big_bullets)
		if stats.game_active:
			if not count%int((tim/stats.level)):
				new_alien = Alien(screen,game_setting,int(random()*(game_setting.screen_width-100)))
				aliens.add(new_alien)	
			update_screen(game_setting,screen,ship,bullets,aliens,stats,play_button,score,count,big_bullets)
			if not count%5000:
				stats.level+=1
				aliens.empty()
				bullets.empty()
				sleep(1)
				score.prep_level()
			#按钮显示
		else:
			play_button.draw_button()
			score.prep_score()
			score.prep_level()
			score.prep_ships
			score.show_score()
		#让绘制的屏幕可见
		pygame.display.flip()
	
	
run_game()
