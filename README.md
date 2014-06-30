UltraMin
--------
Raspberry Pi-powered theramin-like musical instrument
Use the instructions below and the code provided to make a rudimentary movement-controlled musical instrument.
By moving your hand closer and further away from the sensor, the pitch from the buzzer will change.

Connect the ultrasonic distance sensor to the following pins on your Pi:
* VCC to 5V pin
* GND to Ground pin
* TRIG to pin 23
* ECHO to pin 24 via a 1k resistor

Please note the use of the 1k resistor lowers the voltage returning to your Pi. If you don't use the resistor, 5V will be delivered to your GPIO pin and potentially fry your Pi.

Connect a buzzer to the following pins on your Pi:
* Positive (long leg) to pin 18
* Negative (short leg) to Ground pin

