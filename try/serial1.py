mport serial
import time

# Setup variable
serial_use     = 1
serial_port    = None
Read_Rx        = 0
receiving_exit = 1
threding_Time  = 0.01

# Send data by one byte
def TX_data(ser, one_byte):
    ser.write(serial.to_bytes([one_byte]))

# Recive data
def RX_data(ser):
    # if ser.inWaitting() > 0: inWaitting -> in_waiting changed in version 3.0
    # Return the number of bytes in the receive buffer
    if ser.in_waiting() > 0:
        # read(1) == 1 byte data read from the port
        result = ser.read(1)
        RX = ord(result)
        return RX
    else:
        return 0

# Main Function
# This code is not excute when imported other code
if __name__ == '__main__':
    BPS = 4800
    
    serial_port = serial.Serial('/dev/ttyS0', BPS, timeout = 0.01)
    serial_port.flush() # Clear buffer

    TX_data(serial_port, 128)

    time.sleep(1)

    print("Return DATA : " + str(RX_data(serial_port)))
    
    exit(1)


