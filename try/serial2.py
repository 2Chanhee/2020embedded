import serial

ser = serial.Serial('/dev/ttyAMA0', 4800, timeout = 0.001)
ser.open
ser.flush
