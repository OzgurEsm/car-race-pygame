import pygame
from pygame.locals import * 
import random

size = width, height = (800,800)

pygame.init()
screen = pygame.display.set_mode(size)




def play():
    road_width = int(width/1.6) 
    roadmark_width = int(width/80) 
    right_lane = width/2 + road_width/4 
    left_lane = width/2 - road_width/4 
    speed = 3
    running = True 
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Pygame P1 Racing') 
    screen.fill((200,150,250)) 

    pygame.display.update() 

    my_car = pygame.image.load("car1.png") ; 
    my_car_loc = my_car.get_rect() 
    my_car_loc.center =  right_lane, height*0.8 
    other_car = pygame.image.load('car2.png')
    other_car_loc = other_car.get_rect()
    other_car_loc.center = left_lane, height*0.2

    counter = 0
    while running:
        counter += 1
        if counter == 2000:
            speed += 2
            counter = 0
            print(f'Next Level,your current speed: {speed}')
        # other car animation
        other_car_loc[1] += speed  
        
        if other_car_loc[1] > height:
            
            if random.randint(0,1) == 0: 
                other_car_loc.center = right_lane, -200 
            else:
                other_car_loc.center = left_lane, -200 ;"""randomly choosing lanes here, dont forget .center"""

        #Fail condition
        if my_car_loc[0] == other_car_loc[0] and other_car_loc[1] > my_car_loc[1] - 250:
            break
        

        for event in pygame.event.get():
            if event.type == QUIT:
                return main_menu()

            if event.type == KEYDOWN: #pressing key #stopped my_car going of screen by cheking it's lane
                if event.key in [K_a, K_LEFT] and my_car_loc.center[0]== right_lane: #pressing a or left arrow while my_car is on right_lane
                    my_car_loc = my_car_loc.move([-road_width/2, 0]) # new coords in list
                if event.key in [K_d, K_RIGHT] and my_car_loc.center[0]== left_lane:
                    my_car_loc = my_car_loc.move([road_width/2, 0])
                if event.key in [K_w, K_UP]:
                    speed += 1
                    print(f'Your new speed is: {speed}')
        pygame.draw.rect(
        screen,
        (50,50,50),
        (width/2 - road_width/2, 0, road_width, height) 
        ) ; """(x,y,width,height) in tuple centered rectangle coord."""

        pygame.draw.rect(
        screen,
        (255,255,0),
        (width/2 - roadmark_width/2, 0, roadmark_width,height)
        ) ; """Yellow line right in the middle"""

        pygame.draw.rect(
        screen,
        (250,250,250),
        (width/2 - road_width/2 + roadmark_width*2, 0, roadmark_width,height)
        ) ;""" draw left white line """

        pygame.draw.rect(
        screen,
        (250,250,250),
        (width/2 + road_width/2 -roadmark_width*3, 0, roadmark_width,height)
        ) ;"""draw right white line,used relative coordinates all along the way!"""

        screen.blit(my_car, my_car_loc) ;"""draw image,location"""
        screen.blit(other_car,other_car_loc)
        
        
        speed_font = pygame.font.Font(None, 20)
        speed_text = speed_font.render(f'Speed level: {speed}', True, 'black')
        speed_rect = speed_text.get_rect(center=(100,100))
        screen.blit(speed_text, speed_rect)
        pygame.draw.rect(screen,(200,150,250),speed_rect)
        
        pygame.display.update() 

def main_menu():
    pygame.display.set_caption('Menu')
    
    while True:
        screen.blit(pygame.image.load('race-bg.png'), (0,0))
        menu_font = pygame.font.Font(None, 100)
        menu_text = menu_font.render('Welcome', True, 'white')
        menu_rect = menu_text.get_rect(center=(width/2,height*0.3))
        screen.blit(menu_text, menu_rect)
        
        move_font = pygame.font.Font(None, 50)
        move_text = move_font.render('Use "a-d or arrow keys" to move', True, (250,0,250))
        move_rect = move_text.get_rect(center=(width/2,height*0.4))
        screen.blit(move_text, move_rect)
        
        speed_font = pygame.font.Font(None, 50)
        speed_text = speed_font.render('Use "w or arrow key UP" to speed up', True, (0,250,250))
        speed_rect = speed_text.get_rect(center=(width/2,height*0.5))
        screen.blit(speed_text, speed_rect)
        
        enter_font = pygame.font.Font(None, 70)
        enter_text = enter_font.render('Press "Enter" to play', True, 'black')
        enter_rect = enter_text.get_rect(center=(width/2,height*0.6))
        screen.blit(enter_text, enter_rect)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == KEYDOWN:
                if event.key == K_RETURN:
                    play()
                
        pygame.display.update()
main_menu()