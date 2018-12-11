import pygame

def checkCollision(x,y,treasureX,treasureY):
	global screen, textBox
	collisionState = False
	if y >= treasureY and y <= treasureY + 40:
		if x >= treasureX and x <= treasureX + 45:
			collisionState = True
			y = 650
		elif x + 45 >= treasureX and x + 45 <= treasureX + 45:
			collisionState = True
			y = 650
	elif y + 40 >= treasureY and y + 40 <= treasureY + 40:
		if x >= treasureX and x <= treasureX + 45:
			collisionState = True
			y = 650
		elif x + 45 >= treasureX and x + 45 <= treasureX + 45:
			collisionState = True
			y = 650
	return collisionState,y

pygame.init()
screen = pygame.display.set_mode((900,700))

finished = False

x = 450-45/2
y = 650
level = 1
print (pygame.K_SPACE)
playerImage = pygame.image.load("./project/player.png").convert()
playerImage = pygame.transform.scale(playerImage, (45,40))
playerImage = playerImage.convert_alpha()

backGroundImage = pygame.image.load("./project/background.png")
backGroundImage = pygame.transform.scale(backGroundImage,(900,700))
screen.blit(backGroundImage,(0,0))

treasureImage = pygame.image.load("./project/treasure.png")
treasureImage = pygame.transform.scale(treasureImage,(45,40))
treasureImage = treasureImage.convert_alpha()

enemyImage = pygame.image.load("./project/enemy.png")
enemyImage = pygame.transform.scale(enemyImage,(35,30))
enemyImage = enemyImage.convert_alpha()

treasureX = 450-45/2
treasureY = 45

enemyX = 100
enemyY = 590-10

screen.blit(treasureImage,(treasureX,treasureY))
font = pygame.font.SysFont("comicsans",60)
textBox = font.render("Many Coinz!",True,(0,0,0))

enemyNames = {0:'Bob',1:'Jenna',2:'Greg',4:'Larry'}


frame = pygame.time.Clock()
collisionTreasure = False
collisionEnemy = False
movingRight = True

enemies = [(enemyX,enemyY,movingRight)]

name = ""
while finished == False: #while game is not finished
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			finished = True

	pressedKeys = pygame.key.get_pressed()

	enemyIndex = 0
	for enemyX,enemyY,movingRight in enemies:
		if enemyX >= 850-25:
			movingRight = False
		elif enemyX <=50:
			movingRight = True
		if movingRight == True:
			enemyX += 5*level*2
		else:
			enemyX -= 5*level*2
		enemies[enemyIndex] = (enemyX,enemyY,movingRight)
		enemyIndex += 1

	if pressedKeys[pygame.K_UP] == 1:
		y-= 5 
	if pressedKeys[pygame.K_DOWN] == 1:
		y+= 5 
	if pressedKeys[pygame.K_LEFT] == 1:
		x-= 5 
	if pressedKeys[pygame.K_RIGHT] == 1:
		x+= 5 

	# rectOne = pygame.Rect(x,y,30,30)#x,y,width,height
	color = (0,0,255)#rgb
	white = (255,255,255)
	screen.blit(backGroundImage,(0,0))
	screen.blit(treasureImage,(treasureX,treasureY))
	screen.blit(playerImage,(x,y))

	enemyIndex = 0
	for enemyX,enemyY,movingRight in enemies:
		screen.blit(enemyImage,(enemyX,enemyY))
		collisionEnemy,y = checkCollision(x,y,enemyX,enemyY)
		if collisionEnemy == True:
			name = enemyNames[enemyIndex]
			textLose = font.render("You were killed by " +name,True,(255,0,0))
			screen.blit(textLose,(450 - textLose.get_width()/2,350 - textBox.get_height()/2))
			pygame.display.flip()
			frame.tick(1)
		enemyIndex += 1

	collisionTreasure,y = checkCollision(x,y,treasureX,treasureY)
	if collisionTreasure == True:
		level += 1
		enemies.append((enemyX-50*level,enemyY-50*level,False))
		textBox = font.render("You've reached level " + str(level),True,(0,0,0))
		screen.blit(textBox,(450 - textBox.get_width()/2,350 - textBox.get_height()/2))
		pygame.display.flip()
		frame.tick(1)
	# pygame.draw.rect(screen,color,rectOne)
	pygame.display.flip()
	frame.tick(24)