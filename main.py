import pygame
import time
from pygame import mixer

#Initialization
pygame.init()

#Screen creation
screen = pygame.display.set_mode((1000,700))

'''Background sound'''
mixer.music.load("fm-freemusic-give-me-a-smile.mp3")
mixer.music.play(-1)

#landing page image
land_image = pygame.image.load("land_image.jpg")

#page_2
char_s_image = pygame.image.load("Premium-Vector-Happy-cute-little-kid-study-alphabet-character.png")
char_s_image_status = 0

#page_3
char_s_scene = pygame.image.load("first_image.jpg")
char_s_scene_status = 0

#page4
char_a_image = pygame.image.load("char_a_image.png")
char_a_image_status = 0

#Setting the Title
pygame.display.set_caption("Sakshar Game By Anushk Gupta and Aatif Ahmad")

#Setting the icon
icon_image = pygame.image.load("languages.png")
pygame.display.set_icon(icon_image)

#Sun Image Load
sun_image = pygame.image.load("final_sun_image.png")

#Snake Image Load
snake_image = pygame.image.load("snake.png")

#Swing Image Load
swing_image = pygame.image.load("swing.png")

#Stone Image Load
stone_image = pygame.image.load("stone_image.png")

#font for the text of the buttons
font = pygame.font.Font("freesansbold.ttf",28)

#winner image load
winner_image = pygame.image.load("46141 (1).jpg")

#sakshar image
sakshar_image = pygame.image.load("SAKSHAR.jpg")


def music_play():
    mixer.music.load("fm-freemusic-give-me-a-smile.mp3")
    mixer.music.play(-1)

def music_stop():
    mixer.music.stop()

def sound_play():
    level_complete_sound = mixer.Sound("success-1-6297.mp3")
    level_complete_sound.play()



#the button class with init method having parameters as text, x-y coordinates, button enabling, height and width
class Button:
    def __init__(self,text,x_pos,y_pos,enabled,height,width):
        self.text = text
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.enabled = enabled
        self.height = height
        self.width = width
        # self.draw()

    #function to draw the button
    def draw(self):
        button_text = font.render(self.text, True, "white")
        button_rect = pygame.rect.Rect((self.x_pos,self.y_pos),(self.width,self.height))
        pygame.draw.rect(screen,"#f07e0c",button_rect,0,5)
        screen.blit(button_text,(self.x_pos + 5,self.y_pos + 10))

    #function to check the button click
    def check_click(self):
        mouse_pos = pygame.mouse.get_pos()
        left_click = pygame.mouse.get_pressed()[0]
        button_rect = pygame.rect.Rect((self.x_pos,self.y_pos),(self.width,self.height))
        if left_click and button_rect.collidepoint(mouse_pos) and self.enabled:
            return True
        else:
            return False

#Beginning status of several elements which will be modified as per the transitions of the game
input_1 = True
input_2 = False
char_s_scene_status = 0
sun_image_status = 0
snake_image_status = 0
swing_image_status = 0
stone_image_status = 0
second_char_status = 0
sound_play_status = 1
music_play_status = 0




control = True #status of the main while loop
while control: #main running loop of the game screen
    
    my_button_3 = Button("SUN",240,15,True,150,130)
    my_button_3.draw()

    my_button_4 = Button("SNAKE",800,550,True,200,150)
    my_button_4.draw()

    my_button_5 = Button("SWING",500,200,True,240,150)
    my_button_5.draw()

    my_button_6 = Button("STONE",50,500,True,150,150)
    my_button_6.draw()

    screen.blit(land_image,(0,0))
    screen.blit(sakshar_image,(270,5))

    my_button_1 = Button("LET US PLAY",430,590,True,50,190)
    my_button_1.draw()
    input_1 = my_button_1.check_click()
    if input_1:
        char_s_image_status = 1

    my_button_2 = Button("NEXT",470,90,True,50,90)
    
    if char_s_image_status == 1:
        screen.fill((255,255,255))
        screen.blit(char_s_image,(180,170))
        my_button_2.draw()
        input_2 = my_button_2.check_click()
        if input_2:
            char_s_scene_status = 1
    
    if char_s_scene_status == 1:
        screen.blit(char_s_scene,(0,0))
        input_3 = my_button_3.check_click()
        if input_3:
            sun_image_status = 1
        
        input_4 = my_button_4.check_click()
        if input_4:
            snake_image_status = 1

        input_5 = my_button_5.check_click()
        if input_5:
            swing_image_status = 1

        input_6 = my_button_6.check_click()
        if input_6:
            stone_image_status = 1
    
    #blitting the images of elements on the screen after their positions are clicked
    if sun_image_status == 1:
        screen.blit(sun_image,(180,-6))
        
        
    if snake_image_status == 1:
        screen.blit(snake_image,(724,507))
        

    if swing_image_status == 1:
        screen.blit(swing_image,(480,160))
        

    if stone_image_status == 1:
        screen.blit(stone_image,(-10,480))

    if sun_image_status == 1 and snake_image_status == 1 and swing_image_status == 1 and stone_image_status == 1:
        
        screen.fill((255,255,255))
        screen.blit(winner_image,(120,70))
        if sound_play_status == 1:
            sound_play()
            sound_play_status = 0
        my_button_3 = Button("NEXT",475,590,True,50,90)
        my_button_3.draw()
        input_7 = my_button_3.check_click()
        if input_7:
            second_char_status = 1
        
    if second_char_status == 1:
        
        screen.fill((255,255,255))
        screen.blit(char_a_image,(125,150))
        my_button_4 = Button("NEXT",450,93,True,50,90)
        my_button_4.draw()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            control = False #ensuring that the screen ends only when the quit event is pressed

    pygame.display.update()

    