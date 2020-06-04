import pygame
import random
import time

#snake structure
def snake(snake_list ,blue ,snake_body ):
    for i in snake_list:
        pygame.draw.rect( disp , blue ,[ i[0] , i[1] ,snake_body ,snake_body] )


#init
pygame.init()
clock = pygame.time.Clock()

#colors
black = (0,0,0)
white = (255,255,255)
red = (255 , 0 , 0)
blue = ( 0 , 0 , 240)


#game dimensions
width = 500
height = 500
disp =pygame.display.set_mode((width ,height))
pygame.display.set_caption("SNKEVV")
snake_body =10

#main game loop
def game():
    #snake pos 
    snake_pos_x = ((width /4)/10) *10.0 
    snake_pos_y = ((height/4)/10) *10.0
    #change
    mov_x = 0
    mov_y = 0
    play = True
    
    snake_list = []
    snake_length = 1
    speed =10
    #food
    food_x = round(random.randint(1,width)/10.0)*10.0
    food_y = round(random.randint(1,height)/10.0)*10.0



    while play:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                play =False
            #snake mov
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    mov_x -=snake_body  
                    mov_y = 0 
                elif event.key == pygame.K_RIGHT:
                    mov_x +=snake_body  
                    mov_y = 0
                elif event.key == pygame.K_DOWN:
                    mov_x = 0  
                    mov_y += snake_body
                elif event.key == pygame.K_UP:
                    mov_x =0  
                    mov_y -=snake_body
        if snake_pos_x > width or snake_pos_x < 0 or snake_pos_y > height or snake_pos_y <0:
            play = False
            
        snake_pos_x += mov_x
        snake_pos_y += mov_y                                    
        
        disp.fill(black)

        #food
        pygame.draw.rect( disp ,red ,[ food_x , food_y ,snake_body ,snake_body] )
        snake_head = []
        snake_head.append(snake_pos_x)
        snake_head.append(snake_pos_y)
        snake_list.append(snake_head)

        snake(snake_list , blue ,snake_body)        

        pygame.display.update()    

        if snake_pos_x == food_x and snake_pos_y == food_y:
            food_x = round(random.randint(1,width)/10.0)*10.0
            food_y = round(random.randint(1,height)/10.0)*10.0
            snake_length+=1

        if len(snake_list) > snake_length:
            del snake_list[0]

        for i in  snake_list[:-1]:
            if i == snake_head:
                play =False
        clock.tick(speed)
    pygame.quit()
    quit()

game()
