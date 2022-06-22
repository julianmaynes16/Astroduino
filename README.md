# Astroduino
Arduino project based on making a star tracker that can track heavenly bodies.

# Instructions
1. Launch FirmataComms and upload this to an arduino board through the Arduino IDE. 
2. Build the tracking module. Needed for this step are an Arduino, two continuous servo motors, (preferably) a breadboard, and (preferably) an LED. Digital pin 13 powers an LED that acts as a diagnostic to tell when motors are being activated. Digital pin 11 powers to the bottom azimuth motor, and digital pin 10 powers the top altitude motor. Please refer to the sample setup if you have questions on the setup
3. Launch the Astroduino_Coords program and input your date, time, location, and desired object. This program calculates the altitude and azimuth of the object and returns two time values. Copy each down.
4. Position the motors such that the top motor's head is facing directly north and level with the top motor.
5. Launch the Astroduino_Azimuth program and replace the number seen in line 24 with the azimuth number given in the Astroduino_Coords program and run the program. The bottom motor should move.
6. Launch the Astroduino_Altitude program and replace the number seen in line 24 with the altitude number given in the Astroduino_Coords program. The top motor should move. 
7. The top motor should be facing the desired object! To track another object, reinput your information and reposition the motor head back to the north and level with the motor.

# Status

06/22/22 - This software is a work in progress. The pointer will point near an object, but it will be severely off. I am just working on calibration, which will be done soon!

# Contact

Have any questions? Feel free to contact me! 
Email: thelastpocket@gmail.com
