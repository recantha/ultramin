# Raspberry Pi Theramin-like musical instrument
# Written by Michael Horne
# 1st July 2014
# Feel free to take and adapt the code. A reference back to my blog at
# http://www.recantha.co.uk/blog would be appreciated if you publish it.

# Import your libraries
import RPi.GPIO as GPIO
import time
import threading

# Define constants
# Ultrasonic
PIN_TRIG=23
PIN_ECHO=24

# Define buzzer, including initial frequencies
# We set the buzzer going straight away so we have to set an initial frequency
# We also set a multiplier for the frequency so we can have bigger range of tones
PIN_BUZZER = 18
BASE_FREQUENCY = 300
FREQUENCY_MULTIPLIER = 2

# Function to read ultrasonic sensor
def read_ultrasonic():
	# Switch the trigger pin on and off very quickly
	# This is what the sensor expects and tells it to send the pulse
	GPIO.output(PIN_TRIG, True)
	time.sleep(0.00001)
	GPIO.output(PIN_TRIG, False)

	# Wait for the echo pin to go low (i.e. it's waiting)
	signal_off = 0
	signal_on = 0
	while GPIO.input(PIN_ECHO) == 0:
		signal_off = time.time()

	# Wait for the echo pin to go high (i.e. it's received the ping)
	while GPIO.input(PIN_ECHO) == 1:
		signal_on = time.time()

	# Work out how long it took for the ping to go out and back
	time_passed = signal_on - signal_off

	# Speed of sound calculation to work out distance
	distance = time_passed * 34000

	# That was the distance there and back so halve it to get true distance
	distance = distance/2

	# Print the distance out. You CAN comment this out if you don't care
	# to see the distance read-out
	print distance

	return distance

# Some things it's just nicer to have inside a function
def setup():
	# Set-up GPIO
	GPIO.setwarnings(False)
	GPIO.setmode(GPIO.BCM)

	# Set-up ultrasonic sensor
	GPIO.setup(PIN_TRIG, GPIO.OUT)
	GPIO.setup(PIN_ECHO, GPIO.IN)
	GPIO.output(PIN_TRIG, False)
	# Let sensor settle
	time.sleep(0.5)

	# Set-up buzzer
	GPIO.setup(PIN_BUZZER, GPIO.OUT)

# Wrapper to change frequency of buzzer via PWM
def change_frequency(freq):
	p.ChangeFrequency(freq)

######################################################

# Run set-up and set-up the PWM for the buzzer
setup()
p = GPIO.PWM(PIN_BUZZER,BASE_FREQUENCY)
p.start(1)

# Infinite loop to read distance and change frequency of buzzer
# based on the reading
try:
	while True:
		distance = read_ultrasonic()
		time.sleep(0.1)
		change_frequency(BASE_FREQUENCY+(distance*FREQUENCY_MULTIPLIER))

except KeyboardInterrupt:
	# Ctrl-C exits the program here
	pass

# Don't forget to cleanup otherwise the buzzer won't stop!
GPIO.cleanup()
