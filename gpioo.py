import RPi.GPIO as GPIO
sayac = 0


if GPIO.input(29):
    sayac = sayac + 1
