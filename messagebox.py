import  time
import pygame
from tkinter import *
from tkinter import messagebox

Tk().wm_withdraw()

pygame.init()

screen = pygame.display.set_mode((500, 150))
pygame.display.set_caption('Закрий')
font = pygame.font.SysFont("",20)
label = font.render("Закрий" ,1, (12, 140, 0, 1))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            time.sleep(0.01)
            screen = pygame.display.set_mode((500, 150))
            pygame.display.set_caption('Закрий')
            messagebox.showerror( "Закрий    " , "Нажми ок")

    screen.fill((0, 0, 0))
    screen.blit(label, (50, 50))
    pygame.display.update()
