import pygame
from pygame.locals import DOUBLEBUF
import sys
import Names
import Attack

#Global constants
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
FRAMES_PER_SEC = 60
#Player dimensions
PLAYER_WIDTH = 40
PLAYER_HEIGHT = 60
#Player movement speed
SPEED = 5

#Colors
GRAY = (128, 128, 128)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)

def start():
    #Initialize pygame
    pygame.init()
    
    #Set the window caption
    pygame.display.set_caption("wow! really good!!")
    
    #Use double buffering for better performance
    flags = DOUBLEBUF
    #Create the screen
    global screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), flags)
    
    #Create the clock
    global clock
    clock = pygame.time.Clock()
    
    global player_pos
    player_pos = [(SCREEN_WIDTH - PLAYER_WIDTH) / 2, (SCREEN_HEIGHT - PLAYER_HEIGHT) / 2]
    
    global names
    names = Names.NameGenerator("name_parts.json")
    
    #Start the game loop
    run()

def run():
    while True:
        clock.tick_busy_loop(FRAMES_PER_SEC)
        update()
        render()

def update():
    pressed = pygame.key.get_pressed()
    
    if pressed[pygame.K_ESCAPE]:
        sys.exit(0)
    
    if pressed[pygame.K_LEFT] or pressed[pygame.K_a]:
        player_pos[0] -= SPEED
    if pressed[pygame.K_RIGHT] or pressed[pygame.K_d]:
        player_pos[0] += SPEED
    if pressed[pygame.K_UP] or pressed[pygame.K_w]:
        player_pos[1] -= SPEED
    if pressed[pygame.K_DOWN] or pressed[pygame.K_s]:
        player_pos[1] += SPEED
    
    for event in pygame.event.get():
        if event.type == pygame.locals.QUIT:
            sys.exit(0)
        
        elif event.type == pygame.locals.KEYDOWN:
            if event.key == pygame.K_SPACE:
                for _ in range(10):
                    print(names.generate_name())
        
        elif event.type == pygame.locals.MOUSEBUTTONDOWN:
            if event.button == 1:
                #attack
                print("attack")
            elif event.button == 3:
                #right click
                pass

def render():
    #Draw a gray background
    screen.fill(GRAY)
    
    #Draw the player as a pink rectangle
    player_rect = pygame.rect.Rect(player_pos, (PLAYER_WIDTH, PLAYER_HEIGHT))
    pygame.draw.rect(screen, MAGENTA, player_rect)
    
    #Update the display
    pygame.display.update()