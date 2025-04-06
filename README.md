# simulating force feedback on mouse
 
This project explores an innovative approach to force feedback simulation using telemetry data from Assetto Corsa's shared memory. The goal is to use the force feedback data to modify the virtual mouse axis via vJoy, then feed the adjusted mouse input back into the simulator to alter the virtual steering wheel's position. I have made an attempt to simulate this behavior, but I can’t seem to make it work properly.

In this project, I utilize vJoy (a virtual joystick driver), a mouse hider implemented using AutoHotkey, and FreePIE (a Programmable Input Emulator) to create and manage force feedback effects for the mouse.

https://andersmalmgren.github.io/FreePIE/
https://sourceforge.net/projects/vjoystick/
