import serial
ser = serial.Serial('/dev/ttyUSB0', baudrate = 9600, timeout = 10)
c3 = b'00H3300000'
ser.write(c3)
out = ser.readline()

