import RPi.GPIO as GPIO
import urllib.request
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

gpio = 26
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

rly1 = 26
rly2 = 19
rly3 = 13
rly4 = 6

GPIO.setup(rly1, GPIO.OUT)
GPIO.setup(rly2, GPIO.OUT)
GPIO.setup(rly3, GPIO.OUT)
GPIO.setup(rly4, GPIO.OUT)

GPIO.output(rly1, 1)
GPIO.output(rly2, 1)
GPIO.output(rly3, 1)
GPIO.output(rly4, GPIO.OUT)

prv = ''

while True:
    r_link = 'https://api.thingspeak.com/channels/394000/fields/1/last?api_key=KXGTQ0C0ZEFG2EOW'
    f = urllib.request.urlopen(r_link)
    rcv = (f.readline()).decode()

    if prv != rcv:
        prv = rcv

        if rcv[0] == 'A':
            print('D1 ON ')
            GPIO.output(rly1, 0)

        if rcv[0] == 'B':
            print('D2 ON')
            GPIO.output(rly2, 0)

        if rcv[0] == 'C':
            print('D3 ON')
            GPIO.output(rly3, 0)

        if rcv[0] == 'D':
            print('D1 OFF')
            GPIO.output(rly1, 1)

        if rcv[0] == 'E':
            print('D2 OFF')
            GPIO.output(rly2, 1)

        if rcv[0] == 'F':
            print('D3 OFF')
            GPIO.output(rly3, 1)

        if rcv[0] == 'G':
            print('D4 ON')
            GPIO.output(rly4, 0)

        if rcv[0] == 'H':
            print('D4 OFF')
            GPIO.output(rly4, 1)
