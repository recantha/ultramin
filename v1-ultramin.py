import time
import sys
import RPi.GPIO as GPIO
import math
import pyaudio

PIN_TRIG=23
PIN_ECHO=24

PyAudio = pyaudio.PyAudio
pyaudio = PyAudio()

RATE = 16000

def setup():
	GPIO.setwarnings(False)
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(PIN_TRIG, GPIO.OUT)
	GPIO.setup(PIN_ECHO, GPIO.IN)
	GPIO.output(PIN_TRIG, False)
	# Let U/S settle
	time.sleep(0.5)

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

def tone(WAVE):
	data = ''.join([chr(int(math.sin(x/((RATE/WAVE)/math.pi))*127+128)) for x in xrange(RATE)])

	stream = pyaudio.open(format = pyaudio.get_format_from_width(1),
			channels = 1,
			rate = RATE,
			output = True
		)

#	for DISCARD in xrange(5):
	stream.write(data)

	stream.stop_stream()
	stream.close()


#########################################

setup()
while True:
	distance = read_ultrasonic()
	tone(distance*100)

GPIO.cleanup()
pyaudio.terminate()


