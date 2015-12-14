#!/usr/bin/python
#
# Call like this:
# 
# ./CBT-PrintDebug.py /dev/ttyACM0
#
#
import sys
import serial

ser = serial.Serial(sys.argv[1], 115200, timeout=1)
ser.open()
ser.write('\x01\x01')

print('\n')
print(ser.read(4096))	

ser.close()