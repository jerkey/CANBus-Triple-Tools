#!/usr/bin/python
#
# Call like this:
# 
# ./CBT-LogFilterBus3.py /dev/ttyACM0
#
#
import sys
import serial

ser = serial.Serial(sys.argv[1], 115200, timeout=1)
ser.open()
ser.write('\x04\x03')

print('\n')
print(ser.read(4096))	

ser.close()