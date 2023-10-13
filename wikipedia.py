#!/usr/bin/python

import os
import random
import pygame
import RPi.GPIO as GPIO

SAMPLES = os.listdir('samples')


def button_callback(channel):
    playing = pygame.mixer.music.get_busy()
    pygame.mixer.music.stop()
    if playing:
        return

    index = random.randint(0, len(SAMPLES)-1)
    print(SAMPLES[index])
    pygame.mixer.music.load("samples/" + SAMPLES[index])
    pygame.mixer.music.play()
    print("Button was pushed!")

pygame.mixer.init()

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.add_event_detect(10, GPIO.RISING, callback=button_callback, bouncetime=400)
message = input("Press enter to quit\n\n")
GPIO.cleanup()
