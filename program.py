## AUTHOR: Garima
## TASK : 5.2C (To create simple GUI interfaces with Raspberry Pi, to turn on one of three LED lights)

from tkinter import*
import tkinter.font
from gpiozero import LED
import RPi.GPIO
 
RPi.GPIO.setmode(RPi.GPIO.BCM)

red_led = LED(7)
blue_led = LED(15)
green_led = LED(11)

window = Tk()

window.title("LED Toggler")
normalFont = tkinter.font.Font(size = 14, weight = "bold")

def Toggle_red():
	if red_led.is_lit:
		red_led.off()
		redButton["text"] = "Red LED"
	else:
		red_led.on()
		blue_led.off()
		blueButton["text"] = "Blue LED"
		green_led.off()
		greenButton["text"] = "Green LED"
		redButton["text"] = "Turn off"

def Toggle_blue():
	if blue_led.is_lit:
		blue_led.off()
		blueButton["text"] = "Blue LED"
	else:
		blue_led.on()
		green_led.off()
		greenButton["text"] = "Green LED"
		red_led.off()
		redButton["text"] = "Red LED"
		blueButton["text"] = "Turn off"

def Toggle_green():
	if green_led.is_lit:
		green_led.off()
		greenButton["text"] = "Green LED"
	else:
		green_led.on()
		greenButton["text"] = "Turn off"
		blue_led.off()
		blueButton["text"] = "Blue LED"
		red_led.off()
		redButton["text"] = "Red LED"

def reset():
    blue_led.off()
    green_led.off()
    red_led.off()

def exit():
    RPi.GPIO.cleanup()
    window.destroy()

redButton = Button(window, font = normalFont, command = Toggle_red, text = 'Red LED', bg = 'red', height = 1, width = 20)
blueButton = Button(window, font = normalFont, command = Toggle_blue, text = 'Blue LED' ,bg = 'blue', height = 1, width = 20)
greenButton = Button(window, font = normalFont, command = Toggle_green, text = 'Green LED', bg = 'green', height = 1, width = 20)
resetButton = Button(window, text = 'Reset', font = normalFont, command = reset, bg = 'pink', height = 1, width = 15)
exitBotton = Button(window, text = 'Exit', font = normalFont, command = exit, bg = 'pink', height = 1, width = 10)
redButton.grid(row = 0, column = 0)
blueButton.grid(row = 1, column = 0)
greenButton.grid(row = 2, column = 0)
resetButton.grid(row = 3, column = 0)
exitBotton.grid(row = 4, column = 0)