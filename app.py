import pygame
import game_config as gc
from pygame import display, event, image
from Animal import Animal
from time import sleep
def find_index(x,y):
    row = y // gc.Image_size
    col = x // gc.Image_size
    index = row * gc.side_tiles + col
    return index

pygame.init()
size = width,height = 512,512
screen = pygame.display.set_mode(size)
run = True

background = image.load("background.jpg")
display.set_caption("Match Game")
match = image.load("matched.png")
win = image.load("youwin.jpg")

Animalcards = [ Animal(i) for i in range (0, gc.total_tiles) ]
current_images = []
total_skips = 0
while run:
    if total_skips == len(Animalcards):
        screen.blit(win,(0,-0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False
                break
            
        if event.type == pygame.MOUSEBUTTONDOWN :
            mouse_x, mouse_y = pygame.mouse.get_pos()
            index = find_index(mouse_x,mouse_y)
            current_images.append(index)
            if len(current_images) > 2:
                current_images = current_images[1:]

    for _, card in enumerate(Animalcards):
        if card.index in current_images:
            image_i = card.image
        else:
            image_i = card.box
        if not card.skip:
            screen.blit(image_i, (card.col * gc.Image_size,card.row * gc.Image_size))
    display.flip()

    if len(current_images) == 2:
        if Animalcards[current_images[0]].name ==Animalcards[current_images[1]].name and not(current_images[0] == current_images[1]):
            Animalcards[current_images[0]].skip = True
            Animalcards[current_images[1]].skip = True
            screen.blit(match, (0,0))
            sleep(0.7)
            display.flip()
            sleep(0.4)
            current_images = []
            total_skips +=2
    screen.blit(background,(-10,-10))

pygame.quit()
