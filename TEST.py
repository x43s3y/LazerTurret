import pygame
from pygame.locals import *
import time
import serial

pygame.init()
canvasMeasure = 180
pygame.display.set_mode((canvasMeasure, canvasMeasure))
pygame.display.set_caption("ControlLazer")
running = True


while running:
    for event in pygame.event.get():
        if event.type == quit:
            running = False
        if event.type == KEYDOWN and event.key == K_ESCAPE:
            running = False
        if event.type == MOUSEBUTTONDOWN:
            coordinatesX, coordinatesY = pygame.mouse.get_pos()
            print("x: ", coordinatesX, "y: ", coordinatesY)
            ser = serial.Serial('COM5', 9600) # Establish the connection on a specific port
            time.sleep(2)
            ser.write(b'X{coordinatesX}Y{coordinatesY}')
            ser.close()


pygame.display.quit()