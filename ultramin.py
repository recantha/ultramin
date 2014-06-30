import RPi.GPIO as GPIO
import time
import threading

# Define constants
# Ultrasonic
PIN_TRIG=23
PIN_ECHO=24

# Buzzer, including initial frequencies
# Remember, the buzzing is going to be threaded so we need to set the FREQUENCY as a constant that will be changed by the ultrasonic reading
PIN_BUZZER = 18
FREQUENCY = 300

def read_ultrasonic():
	GPIO.output(PIN_TRIG, True)
	time.sleep(0.00001)
	GPIO.output(PIN_TRIG, False)

	signal_off = 0
	signal_on = 0
	while GPIO.input(PIN_ECHO) == 0:
		signal_off = time.time()

	while GPIO.input(PIN_ECHO) == 1:
		signal_on = time.time()

	time_passed = signal_on - signal_off

	distance = time_passed * 34000
	# That was the distance there and back so halve it to get true distance
	distance = distance/2
	print distance

	return distance

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

def change_frequency(freq):
	p.ChangeFrequency(freq)

######################################################

setup()
p = GPIO.PWM(PIN_BUZZER,FREQUENCY)
p.start(1)

try:
	while True:
		distance = read_ultrasonic()
		time.sleep(0.05)
		change_frequency(200+distance)

except KeyboardInterrupt:
	pass

GPIO.cleanup()
