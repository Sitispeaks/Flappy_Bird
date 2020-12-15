import pygame,sys,random

from pygame import display

pygame.init()  ##initiate pygame

screen=pygame.display.set_mode((550,800)) ##makes a canvas of given width and height respectively
clock=pygame.time.Clock() ##to limit the framerate

# game variables
gravity=0.25
bird_movement=0
game_active=True


##to import images
bg_surface=pygame.image.load('assets/background-day.png').convert()
##doubles the size of new surface
bg_surface=pygame.transform.scale2x(bg_surface)

floor_surface=pygame.image.load('assets/base.png').convert()
floor_surface=pygame.transform.scale2x(floor_surface)


##for bird surface
# 1.import image on Surface
# 2.put rect around surface
# 3.blit(surface,rect)

bird_surface=pygame.image.load('assets/bluebird-midflap.png').convert()
bird_surface=pygame.transform.scale2x(bird_surface)
##it puts a rectangle around  the bird_surface
bird_rect=bird_surface.get_rect(center=(90,400))


# for pipes  process
# 1.import image on Surface
# 2.put rect around surface
# 3.blit(surface,rect
pipe_surface=pygame.image.load('assets/pipe-green.png').convert()
pipe_surface=pygame.transform.scale2x(pipe_surface)
# pipes to put on display screen
pipe_list =[]
# pipe is going to appear in every 1200 milisecond
PIPESPAWN=pygame.USEREVENT
pygame.time.set_timer(PIPESPAWN,1200)

##pipe hgt
pipe_height=[400,500,600]








##to move the floor
floor_x=0
def draw_floor():
    screen.blit(floor_surface,((floor_x,700)))
    screen.blit(floor_surface,((floor_x+550,700)))

##to create and move pipes and draw pipes
def create_pipe():
    random_pipe_pos=random.choice(pipe_height)
    bottom_pipe=pipe_surface.get_rect(midtop=(600,random_pipe_pos))## rect1
    top_pipe=pipe_surface.get_rect(midbottom=(600,random_pipe_pos-300)) #rect2
    return bottom_pipe,top_pipe

def move_pipes(pipes):
    for pipe in pipes:
        pipe.centerx-=5
    return pipes

def draw_pipes(pipes):
    for pipe in pipes:
        if pipe.bottom>=800:
            screen.blit(pipe_surface,pipe)
        else:
            flip_pipe=pygame.transform.flip(pipe_surface,False,True)
            screen.blit(flip_pipe,pipe)


##to check collision
def check_collision(pipes):
    for pipe in pipes:
        if bird_rect.colliderect(pipe):
            # print("coolision")
            return False
    
    if bird_rect.top<=-100 or bird_rect.bottom>=700:
        # print("collision")
        return False
    
    else:
        return True




##make  a game loop to open the screen for all time,unless a constraint is given
## all the logics are inside the game loop
while True:
##event loop is used to run the events
    for event in pygame.event.get():  ##it looks for all the events that someone has defined

        ##for quit event
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        # for keydown event
        if  event.type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE:
                # print('flap')
                # when the event is fired ,the bird_movement variable changes
                bird_movement=0
                bird_movement-=12
            
            if event.key==pygame.K_SPACE and game_active==False:
                game_active=True
                pipe_list.clear()
                bird_rect.center=(90,400)
                bird_movement=0

 

        # for PIPESPAWN
        if event.type==PIPESPAWN:
            pipe_list.extend(create_pipe()) ## it contains a pair of pipes
            # print(pipe_list)

 
##it draws a new surface onto the screen surface
    screen.blit(bg_surface,(0,0)) ##move 100px from left and 200px frm top
    
    if game_active:

        ##Bird
        bird_movement+=gravity
        bird_rect.centery+=bird_movement
        screen.blit(bird_surface,bird_rect)
        ## to move the floor for seamless motion
        ##it is moving 1 by per gameloop
        game_active=check_collision(pipe_list)

        #pipes
        pipe_list=move_pipes(pipe_list)
        draw_pipes(pipe_list)


       
    ##floor
    floor_x-=1
    # screen.blit(floor_surface,((floor_x,650)))
    draw_floor()
    # for seamless motion logic here
    if floor_x<=-550:
        floor_x=0

    pygame.display.update()
    clock.tick(120) #it is for framerates





