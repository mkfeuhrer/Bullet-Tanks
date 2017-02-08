import pygame
import time
import random

pygame.init()

white = (255,255,255)
black = (0,0,0)
green = (0,150,0)
light_green = (0,255,0)
red = (150,0,0) 
light_red = (255,0,0)
yellow = (200,200,0)
light_yellow = (255,255,0)
display_width = 800
display_height = 600


gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Bullet Tanks')

#icon = pygame.image.load('./apple2.jpg')
#pygame.display.set_icon(icon)

#img = pygame.image.load('./snakehead2.jpeg')
#appleimg = pygame.image.load('./apple2.jpg')

FPS = 10

smallfont = pygame.font.SysFont("comicsansms" , 25)
medfont = pygame.font.SysFont("comicsansms" , 45)
largefont = pygame.font.SysFont("comicsansms" , 65)

clock = pygame.time.Clock()

def pause():
	paused = True
	message_to_screen("Paused",black,-100,size="large")
	message_to_screen("Press c to continue , q to quit",black,25)
	pygame.display.update()
	while paused:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_c:
					paused = False

				elif event.key == pygame.K_q:
					pygame.quit()
					quit()
		#gameDisplay.fill(white)
		clock.tick(5)				

def button(text,x,y,width,height,inactive_color,active_color):
	cur = pygame.mouse.get_pos()

	if x+width > cur[0] > x and y + height > cur[1] > y:
		pygame.draw.rect(gameDisplay,active_color ,(x,y,width,height))
	else:
		pygame.draw.rect(gameDisplay,inactive_color ,(x,y,width,height))	

	text_to_button(text,black,x,y,width,height)

def score(score):
	text = smallfont.render("Score: "+str(score),True,black)
	gameDisplay.blit(text,[0,0])

def game_intro():

	intro = True

	while intro:

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_c:
					intro = False
				if event.key == pygame.K_q:
					pygame.quit()
					quit()		


		gameDisplay.fill(white)
		message_to_screen("Welcome to Bullet Tanks",green,-100,"large")
		message_to_screen("The objective of the game is to shoot and destroy ",black,-30)
		message_to_screen("the enemy before you are destroyed",black,10)
		message_to_screen("More you destroy , harder the game gets",black,50)
		#message_to_screen("Press c to play again ,Press p to pause or q to quit",black,90,size = "medium")
		

		button("play",150,500,100,50,green,light_green)
		button("controls",350,500,100,50,yellow,light_yellow)
		button("quit",550,500,100,50,red,light_red)


		pygame.display.update()
		clock.tick(10)

def text_objects(text,color,size):
	if size == "small":
		textSurface = smallfont.render(text , True , color)
	elif size == "medium":
		textSurface = medfont.render(text , True , color)	
	elif size == "large":
		textSurface = largefont.render(text , True , color)	
	return textSurface , textSurface.get_rect()

def text_to_button(msg,color,buttonx,buttony,buttonwidth,buttonheight,size="small"):
	textSurf,textRect = text_objects(msg,color,size)
	textRect.center = (buttonx + (buttonwidth/2) , buttony + (buttonheight/2))
	gameDisplay.blit(textSurf,textRect)
	

def message_to_screen(msg,color,y_displace=0,size = "small"):
	textSurf, textRect = text_objects(msg,color,size)
	textRect.center = (display_width/2) , ((display_height/2) + y_displace)
	gameDisplay.blit(textSurf,textRect)
	#pygame.display.update();

def gameLoop():
	global direction
	direction = "right"
	gameExit = False
	gameOver = False
	while not gameExit:

		if gameOver == True:
			message_to_screen("Game Over",red,y_displace=-50,size = "large")
			message_to_screen("Press c to play again ,Press q to quit",black,50,size ="medium" )
			pygame.display.update()

		while gameOver == True:
			#gameDisplay.fill(white)
			

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					gameOver = False
					gameExit = True
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_q:
						gameExit = True
						gameOver = False
					if event.key == pygame.K_c:
						gameLoop()	



		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				gameExit = True
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					pass
					
				elif event.key == pygame.K_RIGHT:
					pass
				elif event.key == pygame.K_UP:
					pass
				elif event.key == pygame.K_DOWN:
					pass
				elif event.key == pygame.K_p:
					pause()			

		gameDisplay.fill(white)

		pygame.display.update()					
		clock.tick(FPS)

	pygame.quit()
	quit()
game_intro()
gameLoop()	