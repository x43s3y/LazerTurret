import pygame
from pygame.locals import *
import time
import serial

pygame.init()
canvasMeasure = 600
pygame.display.set_mode((canvasMeasure, canvasMeasure))
pygame.display.set_caption("Control Lazer")
running = True


while running:
    for event in pygame.event.get():
        if event.type == quit:
            running = False
        if event.type == KEYDOWN and event.key == K_ESCAPE:
            running = False
        if event.type == MOUSEMOTION:
            ser = serial.Serial("COM5", 115200, timeout = 5) 
            coordinatesX, coordinatesY = pygame.mouse.get_pos()
            x = round(coordinatesX / (canvasMeasure/180))
            y = round(coordinatesY / (canvasMeasure/180))
            values = f"X{x}Y{y}"
            valuesBytes = values.encode('utf-8')
            print(valuesBytes)
            time.sleep(2)
            ser.write(valuesBytes)
            msg = ser.read(ser.inWaiting())
            
            print("From Arduino: ", msg)
            ser.close()
            
pygame.display.quit()
