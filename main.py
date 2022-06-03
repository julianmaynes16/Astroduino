from pyfirmata import Arduino, SERVO
from time import sleep, time

board = Arduino('/dev/cu.usbmodem14201')

board.digital[10].mode = SERVO


def rotateServo(pin, angle):
    board.digital[pin].write(angle)
    sleep(0.005)


start = time()
end = 0


while True:

    rotateServo(10,0)
    end = time()
    print(end-start)
    # Altitude Time
    if (end-start > 0.10668472491982744): # Replace number with what was given in the previous window
        break

