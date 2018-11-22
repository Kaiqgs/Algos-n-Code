import pygame as pg
from config import *
from cannon import Cannon
from math import atan,degrees
import random

pg.init()
pg.display.set_caption("Desvie!")
gameDisplay = pg.display.set_mode((d_width,d_height))
clock = pg.time.Clock()


score = 0
playing = True
gameover = False


font = pg.font.SysFont(None,25)
def message(msg,color,pos=[d_width/3, d_height/2]):
	text = font.render(msg,True,color)
	gameDisplay.blit(text,pos)

def startMsg(lvl):
	x = d_width/3
	y = d_height/2
	for i in range(200):
		for event in pg.event.get():
			pass
		gameDisplay.fill(white)
		message(f"Welcome to level number {lvl}",black, pos=(x,y))
		x+=.25
		pg.display.update()
		clock.tick(60)

while playing:
	gameover = False
	score = 0
	level = 1
	for shoot_prob, speed, requirements in difficulty:
		startMsg(level)
		mousePos = pg.mouse.get_pos()
		cannon = Cannon("cannon.png","handle.png","cannonball.png",gameDisplay,d_width *0.98,d_height*0.93, speed)
		cannon.updateAngle(mousePos)
		done = False
		roundDone = False
		result = None
		while not done:

			#Events handling;
			for event in pg.event.get():
				if event.type == pg.QUIT:
					done = True
					playing = False


				elif event.type == pg.MOUSEMOTION:
					mp = pg.mouse.get_pos()
					cannon.updateAngle(mp)

				elif event.type == pg.KEYDOWN:
					if event.key == ord('s'):
						cannon.spawnBall()
					if event.key == pg.K_RETURN and gameover:
						done, roundDone = True, True
			#User messaging;
			gameDisplay.fill(white)
			message(f"Score:{cannon.shootedBalls + score}",black, pos=(d_width *0.8,d_height *0.1))
			message("Difficulty: {:.1f}%".format((1 - shoot_prob) * 100),black, pos=(d_width *0.6,d_height *0.1))
			message(f"Speed:{speed}",black,pos=(d_width *0.45,d_height *0.1))

			#Game logic;
			if(not gameover):result = cannon.updateBalls(mousePos)
			else:
				message("Game Over!!! Press enter to try again!",red)
				pg.draw.circle(gameDisplay,blue,mousePos,10)
			
			cannon.drawBalls()
			cannon.draw()


			if(random.random() > shoot_prob and not gameover):cannon.spawnBall()
			if(cannon.shootedBalls > requirements):done = True
			if(result is not None):gameover,mousePos = True,result

			pg.display.update()
			clock.tick(60)


		score += requirements
		level +=1
		if(not playing or roundDone):break
pg.quit()
quit()