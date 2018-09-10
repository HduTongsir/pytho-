# -*- coding: gb2312 -*-
import sys
import pygame
from bullet import Bullet
from big_bullet import BigBullet
from time import sleep
import time
def check_event(game_setting,ship,bullets,screen,play_button,stats,score,big_bullets):
	'''检测按键'''
	for event in pygame.event.get():
			if event.type==pygame.QUIT:
				sys.exit()
			if event.type==pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					ship.left_flag=True
				if event.key == pygame.K_RIGHT:
					ship.right_flag=True
				if event.key == pygame.K_SPACE:
					ship.time_begin=time.time()
				if event.key == pygame.K_RETURN and stats.game_active==False:
					pre_game_start(score, stats)
				if event.key == pygame.K_ESCAPE:
					sys.exit()
			if event.type==pygame.KEYUP:
				if event.key == pygame.K_LEFT:
					ship.left_flag=False
				if event.key == pygame.K_RIGHT:
					ship.right_flag=False
				if event.key == pygame.K_SPACE:
					ship.time_end=time.time()
					if ship.time_end-ship.time_begin<=5:
						new_bullet = Bullet(screen,ship,game_setting)
						bullets.add(new_bullet)
					else:
						new_bullet = BigBullet(screen,ship,game_setting)
						big_bullets.add(new_bullet)
			elif event.type == pygame.MOUSEBUTTONDOWN:
				mouse_x, mouse_y = pygame.mouse.get_pos()
				check_play_button(stats, play_button, mouse_x, mouse_y,score)
def pre_game_start(score,stats):
	score.prep_score()
	score.prep_level()
	score.prep_ships
	score.show_score()
	stats.reset_stats()
	stats.game_active = True
def check_play_button(stats, play_button, mouse_x, mouse_y,score):
	if play_button.rect.collidepoint(mouse_x, mouse_y):
		pre_game_start(score,stats)
def check_high_score(stats, sb):
	if stats.score > stats.high_score:
		stats.high_score = stats.score
		sb.prep_high_score()
def update_screen(game_setting,screen,ship,bullets,aliens,stats,play_button,score,count,big_bullets):
	'''更新屏幕'''
	screen.fill(game_setting.bg_color)#填充颜色
	score.show_score()
	#飞船更新
	ship.update()
	ship.blitme()
	
	#外星人更新
	aliens.update()
	for alien in aliens.sprites():
		alien.blitme()
	
	#子弹更新
	bullets.update()
	for bullet in bullets.copy():
		if bullet.rect.bottom<=0:
			bullets.remove(bullet)
	for bullet in bullets.sprites():
		bullet.blitme()
	
	#大子弹更新
	big_bullets.update()
	for big_bullet in big_bullets.copy():
		if big_bullet.rect.bottom<=0:
			big_bullets.remove(big_bullet)
	for big_bullet in big_bullets.sprites():
		big_bullet.blitme()
		
	#子弹射中外星人
	collisions1 = pygame.sprite.groupcollide(bullets, aliens, True, True)
	collisions2 = pygame.sprite.groupcollide(big_bullets, aliens, False, True)
	if collisions1 or collisions2:
		stats.score += game_setting.alien_points
		score.prep_score()
		check_high_score(stats, score)
		
	#外星人碰到飞船
	for alien in aliens.copy():
		if alien.y>=700:
			stats.ships_left -= 1
			aliens.empty()
			bullets.empty()
			ship.rect.centerx = ship.screen_rect.centerx
			sleep(1.5)
			score.prep_ships()
			if stats.ships_left<=0:
				stats.reset_stats()
				score.prep_ships()
				count=0
				stats.game_active=False
	#按钮显示
	if not stats.game_active:
		play_button.draw_button()
	
	
	#让绘制的屏幕可见
	pygame.display.flip()
	
