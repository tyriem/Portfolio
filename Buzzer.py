#! /usr/bin/python

# Import a library of functions called 'pygame'
import pygame

# Import a library of functions called 'RPI-GPIO'
import RPi.GPIO as GPIO

# Import a library of functions called 'time'
import time

# Import a library of functions called 'pygame.mixer'
import pygame.mixer

GPIO.setmode(GPIO.BCM)

GPIO.setup (4 , GPIO.IN , pull_up_down=GPIO.PUD_UP)
GPIO.setup (18 , GPIO.IN , pull_up_down=GPIO.PUD_UP)

# Start the pygame sound mixer
pygame.mixer.init(48000, -16, 1, 1024)

# Define the sound files
soundA = pygame.mixer.Sound('soundA.wav')
soundB = pygame.mixer.Sound('soundB.wav')

# Initialize the game engine
pygame.init()
 
# Define the colors we will use in RGB format
black = [ 0, 0, 0]
white = [255,255,255]
red = [255, 0, 0]
 
# Set the height and width of the screen
size=[800,600]
screen=pygame.display.set_mode(size)
# Fill the screen White
screen.fill(white)
# Put something in the application Bar
pygame.display.set_caption("                                                                                     Survey Says! Bahamas")

#Load Gameshow Logo
logo = pygame.image.load ( "/home/pi/python_games/SSB/ssb.jpg" )

#Place Gameshow Logo on Screen With BLIT CMD
screen.blit ( logo , ( 0 , 0 ) )

# Set the font for the text. Windows computer so usd Ariel
myfont = pygame.font.SysFont("Ariel", 30)

# Created Variable for the text on the screen
label = myfont.render("Place your Hands on your Buzzers", 1, black)
player1 = myfont.render("Team A", 1, black)
player2 = myfont.render("Team B", 1, black)


# Draw the 2 empty rectangles for the players
pygame.draw.rect(screen, black, (20,200,150,150), 0)
pygame.draw.rect(screen, black, (600,200,150,150), 0)


# put the text on the screen
screen.blit(label, (10, 10))
screen.blit(player1, (20, 150))
screen.blit(player2, (600, 150))


# show the whole thing
pygame.display.flip()

done=False # used to allow exit when you click close on the window
first = 0 # used to signify the first key pressed and stops other being used
waitReset = 0 # Reset section for the while loop

while done==False: # keep going unless I exit application

    # Stay in the loop until one of the 'button' keys is pressed
    while first==0 and done==False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done=True
         
            # User pressed down on a key and it is not the first one
            if event.type == pygame.KEYDOWN and first==0:

                # Figure out which arrow key
                # Check of LEFT arrow key and that it was the first key pressed
                if event.key == pygame.K_LEFT and first==0:
                    pygame.mixer.Sound.play(soundA)
                    pygame.mixer.music.stop()
                    print("left key pressed.") # Print to console
                    pygame.draw.rect(screen, red, (20,200,150,150), 0) # colour rectangle red
                    first=1 # set first to 1 so no other key presses will count
                if event.key == pygame.K_RIGHT and first==0:
                    pygame.mixer.Sound.play(soundB)
                    pygame.mixer.music.stop()
                    print("right key pressed.")
                    pygame.draw.rect(screen, red, (600,200,150,150), 0)
                    first=1
                pygame.display.flip()
                # a 'button' was pressed and shown on screen
                # now got to the reset code

    # loop waiting until the 2 'button' are reset
    waitReset=0
    while waitReset==0 and done == False:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done=True

                # User pressed down on a key
                if event.type == pygame.KEYDOWN:
                # Pressed Return Key which does a reset
                    if event.key == pygame.K_RETURN:
                        print("reset.")
                        # Draw the 4 empty rectangles for the players
                        pygame.draw.rect(screen, black, (20,200,150,150), 0)
                        pygame.draw.rect(screen, black, (600,200,150,150), 0) 
                        first=0
                        waitReset=1
                        pygame.display.flip()
   
        
# Quit in a clean way when done=True
pygame.quit ()