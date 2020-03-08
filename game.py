##########################################
# Program name: game.py
# Written by: Y Taylor
# Date written: 21/01/2020
# This program is a simple game - with a single player, three enemies and one prize.
# To win the player must avoid the enemies and hit the prize or avoid them all till the screen is clear 
##########################################

import pygame # Imports a game library that lets you use specific functions in your program.
import random # Import to generate random numbers. 

# Initialize the pygame modules to get everything started.

pygame.init() 

# The screen that will be created needs a width and a height.

screen_width = 1200
screen_height = 680
screen = pygame.display.set_mode((screen_width,screen_height)) # This creates the screen and gives it the width and height specified as a 2 item sequence.

# This creates the player and gives it the image found in this folder (similarly with the enemy and prize images). 

player = pygame.image.load("image.jpg")
enemy = pygame.image.load("enemy.png")
enemy1 = pygame.image.load("enemy1.png")
enemy2 = pygame.image.load("monster.jpg")
prize = pygame.image.load("prize.jpg")

# Get the width and height of the images in order to do boundary detection (i.e. make sure the image stays within screen boundaries or know when the image is off the screen).

image_height = player.get_height()
image_width = player.get_width()
enemy_height = enemy.get_height()
enemy_width = enemy.get_width()
enemy1_height = enemy1.get_height()
enemy1_width = enemy1.get_width() 
enemy2_height = enemy2.get_height()
enemy2_width = enemy2.get_width() 
prize_height = prize.get_height()
prize_width = prize.get_width()

print("This is the height of the player image: " +str(image_height))
print("This is the width of the player image: " +str(image_width))

# Store the positions of the player, enemies and prize as variables so that you can change them later. 

playerXPosition = 100
playerYPosition = 50
enemy1Xposition = 100
enemy1Yposition = 50
enemyXposition = 100
enemyYposition = 50
enemy2_Xposition = 100
enemy2Yposition = 50
prizeXposition = 150
prizeYposition = 100

# Make the enemies and prize start off screen and at a random y position.

enemyXPosition =  screen_width
enemyYPosition =  random.randint(0, screen_height - enemy_height)
enemy1XPosition =  screen_width
enemy1YPosition =  random.randint(0, screen_height - enemy1_height)
enemy2XPosition = screen_width
enemy2YPosition = random.randint(0, screen_height - enemy2_height)
prizeXPosition = screen_width
prizeYPosition = random.randint(0, screen_height - prize_height)
# This checks if the up or down key is pressed.
# Right now they are not so make them equal to the boolean value (True or False) of False. 
# Boolean values are True or False values that can be used to test conditions and test states that are binary, i.e. either one way or the other. 

keyUp= False
keyDown = False
keyLeft = False
keyRight =  False

# This is the game loop.
# In games you will need to run the game logic over and over again.
# You need to refresh/update the screen window and apply changes to 
# represent real time game play. 

while 1: # This is a looping structure that will loop the indented code until you tell it to stop(in the event where you exit the program by quitting). In Python the int 1 has the boolean value of 'true'. In fact numbers greater than 0 also do. 0 on the other hand has a boolean value of false. You can test this out with the bool(...) function to see what boolean value types have. You will learn more about while loop structers later. 

    screen.fill(0) # Clears the screen.
    screen.blit(player, (playerXPosition, playerYPosition))# This draws the player, enemies and prize image to the screen at the postion specfied. I.e. (100, 50).
    screen.blit(enemy, (enemyXPosition, enemyYPosition))
    screen.blit(enemy1, (enemy1XPosition, enemy1YPosition))
    screen.blit(enemy2, (enemy2XPosition, enemy2YPosition))
    screen.blit(prize, (prizeXPosition, prizeYPosition))
    
    pygame.display.flip()# This updates the screen. 
    
    # This loops through events in the game.
    
    for event in pygame.event.get():
    
        # This event checks if the user quits the program, then if so it exits the program. 
        
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
        # This event checks if the user press a key down.
        
        if event.type == pygame.KEYDOWN:
        
            # Test if the key pressed is the one we want.
            
            if event.key == pygame.K_UP: # pygame.K_UP represents a keyboard key constant as is for the others
                keyUp = True
            if event.key == pygame.K_DOWN:
                keyDown = True
            if event.key == pygame.K_LEFT:
                keyLeft = True
            if event.key == pygame.K_RIGHT:
                keyRight = True        
        
        # This event checks if the key is up(i.e. not pressed by the user).
        
        if event.type == pygame.KEYUP:
        
            # Test if the key released is the one we want.
            
            if event.key == pygame.K_UP:
                keyUp = False
            if event.key == pygame.K_DOWN:
                keyDown = False
            if event.key == pygame.K_LEFT:
                keyLeft = False
            if event.key == pygame.K_RIGHT:
                keyRight = False        
            
    # After events are checked for in the for loop above and values are set,
    # check key pressed values and move player accordingly.
    
    # The coordinate system of the game window(screen) is that the top left corner is (0, 0).
    # This means that if you want the player to move down you will have to increase the y position. 
    
    if keyUp == True:
        if playerYPosition > 0 : # This makes sure that the user does not move the player above the window.
            playerYPosition -= 4
    if keyDown == True:
        if playerYPosition < screen_height - image_height:# This makes sure that the user does not move the player below the window.
            playerYPosition += 4
    if keyLeft == True:
        if playerXPosition > 0 :
            playerXPosition -= 4
    if keyRight == True:
        if playerXPosition < screen_width - image_width: # This makes sure that the user does not move the player to the right of window.
            playerXPosition += 4        

    # Check for collision of the enemy with the player.
    # To do this we need bounding boxes around the images of the player and enemy.
    # We the need to test if these boxes intersect. If they do then there is a collision.
    
    # Bounding box for the player:
    
    playerBox = pygame.Rect(player.get_rect())
    
    # The following updates the playerBox position to the player's position,
    # in effect making the box stay around the player image. 
    
    playerBox.top = playerYPosition
    playerBox.left = playerXPosition
    
    # Bounding box for the prize:
    
    prizeBox = pygame.Rect(prize.get_rect())
    prizeBox.top = prizeYPosition
    prizeBox.left = prizeXPosition

    # Bounding box for the enemy:

    enemyBox = pygame.Rect(enemy.get_rect())
    enemyBox.top = enemyYPosition
    enemyBox.left = enemyXPosition
    
    # Bounding box for enemy1:

    enemyBox1 = pygame.Rect(enemy1.get_rect())
    enemyBox1.top = enemy1YPosition
    enemyBox1.left = enemy1XPosition

    # Bounding box for enemy2:

    enemyBox2 = pygame.Rect(enemy2.get_rect())
    enemyBox2.top = enemy2YPosition
    enemyBox2.left = enemy2XPosition    

    # Test collision of the boxes:
    
    if playerBox.colliderect((enemyBox2)):
        # Display losing status to the user: 
        
        print("You lose!")
       
        # Quite game and exit window: 
        
        pygame.quit()
        exit(0)
         
    if playerBox.colliderect(prizeBox):
        print("You win")
        pygame.quit()
        exit(0) 
    if playerBox.colliderect(enemyBox1):
        print("You loose")
        pygame.quit()
        exit(0)           
    if playerBox.colliderect(enemyBox):
        print("You loose")
        pygame.quit()
        exit(0)        
    # If the enemy is off the screen the user wins the game:
    
    if enemyXPosition <  - enemy_width:
    
        # Display wining status to the user: 
        
        print("You win!")
        
        # Quite game and exit window: 
        pygame.quit()
        
        exit(0)
    
 
    
    # Make enemies and prize approach the player.
    
    enemyXPosition -= 0.25
    enemy2XPosition -= 0.25
    enemy1XPosition -= 0.25
    prizeXPosition -= 0.25
    # ================The game loop logic ends here. =============
  
