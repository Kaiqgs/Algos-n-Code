import pygame as pg
from config import *
from math import sin,cos,radians,degrees,atan

class CannonBall:
	def __init__(self,im,display,x,y,angle, speed):
		self.im = im
		self.body = pg.image.load(im)

		self.display = display
		self.location = (x,y)
		self.x = 0
		self.y = 0
		self.speed = speed
		self.angle = angle
		self.r = 0
		self.rect = self.body.get_rect()

		self.size = self.rect.size

	def isInBound(self):
		return  (0 < self.x + self.size[0] < d_width) and (0 < self.y + self.size[1] < d_height)

	def isTouching(self,p):
		#print(self.rect)
		return self.rect.collidepoint(*p)
		

	def update(self):
		self.r+=self.speed
		
		self.x = self.location[0] - (sin(radians(self.angle)) * self.r) 
		self.y = self.location[1] - (cos(radians(self.angle)) * self.r)
		self.rect.center = (self.x, self.y)
		#print(self.x,self.y, self.r, self.angle)


	def draw(self):
		self.display.blit(self.body, (self.x, self.y))

class Cannon:
	def __init__(self, im,imh,imc,display,x,y,speed):
		self.im = im
		self.imh = imh
		self.imc = imc
		self.display = display
		self.x = x
		self.y = y
		self.speed = speed

		self.balls = []
		self.shootedBalls = 0
		self.BASEANGLE = 70

		self.handle = pg.image.load(imh)
		self.cannon = pg.image.load(im)
		self.rect = self.cannon.get_rect()
		self.rect.center = (x,y)
		
		self.angle = 90
		self.flipx = False
		self.flipy = False


	def rotate(self,angle):
		self.angle = angle

	def updateAngle(self,mp):
			ad = d_height - mp[1]
			op = d_width - mp[0] 
			self.angle = degrees(atan(op/ad)) - self.BASEANGLE

	def spawnBall(self):
		ball = CannonBall(self.imc,self.display,self.x,self.y, self.angle + self.BASEANGLE, self.speed)
		self.balls.append(ball)


	def flip(self, x,y):
		self.flipx = x
		self.flipy = y

	def draw(self):
		c = pg.transform.rotate(self.cannon,self.angle)
		c = pg.transform.flip(c,self.flipx, self.flipy)
		r = c.get_rect()
		r.center = (self.x, self.y)
		#print(len(self.balls), self.angle)
		self.display.blit(c,r)
		self.display.blit(self.handle, (self.x-10, self.y))
		
	def drawBalls(self):
		for ball in self.balls:
			ball.draw()

	def updateBalls(self,mp):
		for i,ball in enumerate(self.balls):
			p = pg.mouse.get_pos()
			ball.update()
			if(ball.isTouching(p)):return p
			ball.draw()
			if not ball.isInBound():
				del self.balls[i]
				self.shootedBalls += 1