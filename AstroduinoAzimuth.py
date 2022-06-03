from pyfirmata import Arduino, SERVO
from time import sleep, time

board = Arduino('/dev/cu.usbmodem14201')

board.digital[11].mode = SERVO


def rotateServo(pin, angle):
    board.digital[pin].write(angle)
    sleep(0.005)


#rotateServo(11,45)
#i = 0
start = time()
end = 0
while True:

      rotateServo(11,0)
      end = time()
      print(end-start)
      # Azimuth time
      if (end-start > 0.524399817019927): # Replace number with what was given in the previous window
        break

