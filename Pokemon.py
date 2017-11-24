import pygame

import pokebase

import random, math, sys



#exit the program

def events():

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            pygame.quit()

            sys.exit()



#defining the display surface

screenWidth = 800

screenHeight = 600

######################

halfScreenWidth = screenWidth/2

halfScreenHeight = screenHeight/2

#################################

SCREEN_AREA = screenWidth * screenHeight

########################################



#initialize the display

pygame.init()

CLOCK = pygame.time.Clock()

SCREEN = pygame.display.set_mode((screenWidth,screenHeight))

FPS = 500



#Defining a list of colors in case they are needed

BLACK = (0, 0, 0)

WHITE = (255, 255, 255)

RED = (255, 0, 0)

BLUE = (0, 0, 255)

GREEN = (0, 255, 0)

#########################

def game_loop():

    #setting the background image and use convert because the pixels of the image may not be the 

    #same as the background. Convert saves time

    pokemonRoute = pygame.image.load('GreatMarsh.png').convert()

    #finding out what the background width and background height are of the pokemon route

    backgroundWidth, backgroundHeight = pokemonRoute.get_rect().size

    #setting the width of the route will stop the player from being able to exit the bounds of the 

    #pokemon route and will stop the background from scrolling out of bounds of the display surface

    routeWidth = backgroundWidth #* 2
    
    routePositionX = 0



    scrollingRoutePositionX = halfScreenWidth



    #this is a circle for now, but can be changed to the player later on

    circleRadius = 25

    circlePositionX = circleRadius



    #difining the player positions

    playerPositionX = circleRadius

    playerPositionY = 345

    #tells the stage what direction to move, added velocity Y for up and down movement

    playerVelocityX = 0
    playerVelocityY = 0




    #setting the game loop done variable to false initially

    done = False

    #main loop

    while not done:

        #calling the events function to see if the user has left the game

        events()



        #finding out what keys have been pressed

        KEY_PRESSED = pygame.key.get_pressed()

        #if the user presses the right key, then move in the positive x direction

        if KEY_PRESSED[pygame.K_RIGHT]:

            playerVelocityX = 1

        #if the user presses the left key, then move in the negative x direction

        elif KEY_PRESSED[pygame.K_LEFT]:

            playerVelocityX = -1
        
        #if the user presses the up key, then move subtract y position
        elif KEY_PRESSED[pygame.K_UP]:
            
            playerVelocityY = -1
        
        #if the user presses the down key, then move add y position
        elif KEY_PRESSED[pygame.K_DOWN]:
            
            playerVelocityY = 1
        #if no key is pressed, then do not move and remain in the same position

        else:

            playerVelocityX = 0
            playerVelocityY = 0
            
        #add velocity for y position for up and down movement
        playerPositionY += playerVelocityY
        playerPositionX += playerVelocityX

        #if the playerposition in the x direction is greater than the width

        #of the route minus the circle radius, then push the player to the 

        #righthand edge of the screen

        if playerPositionX > routeWidth - circleRadius:

            playerPositionX = routeWidth - circleRadius
        #if player reaches height of screen set y position to remain on screen
        elif playerPositionY > screenHeight + 5:
            
            playerPositionY =  screenHeight + 5
            
        #if player reaches starting y = 0 (top left) set position y to remain on screen
        elif playerPositionY < 50:
            
            playerPositionY = 50
            
        #if the playerposition in the x direction is less than the radius

        #of the cirle, then push the player to the lefthand corner of the screen

        elif playerPositionX < circleRadius:

            playerPositionX = circleRadius

        #if the player position in the x direction is less than the scrollingrouteposition

        #then the ball will be located in the center and move with the screen

        elif playerPositionX < scrollingRoutePositionX:

            circlePositionX = playerPositionX

        #if the playerposition is greater than the routewidth minus

        #the scrolling route position in the x direction, then the ball will

        #not be in the center, and it will be located at route width minus

        #the scrolling route position plus the width of the screen

        elif playerPositionX > routeWidth - scrollingRoutePositionX:

            circlePositionX = playerPositionX - routeWidth + screenWidth

        #else the circle is in the middle of the screen

        else:

            circlePositionX = scrollingRoutePositionX

            routePositionX += -playerVelocityX



        relativePositionX = routePositionX % backgroundWidth

        print("Route Position" + str(routePositionX))

        print("Background Width" + str(backgroundWidth))

        print("Relative Position" + str(relativePositionX))

        SCREEN.blit(pokemonRoute, (relativePositionX - backgroundWidth, 0))

        if relativePositionX < screenWidth:

            SCREEN.blit(pokemonRoute, (relativePositionX, 0))





        pygame.draw.circle(SCREEN, WHITE, (playerPositionX, playerPositionY - circleRadius), circleRadius, 0)



        pygame.display.update()

        CLOCK.tick(FPS)

        SCREEN.fill(BLACK)

game_loop()

