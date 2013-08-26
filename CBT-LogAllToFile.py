#!/usr/bin/python
#
# Call like this:
# 
# ./CBT-LogAllToFile.py /dev/ttyACM0 FileToWrite.txt
#
#
import sys
import serial

f = open(sys.argv[2], 'w')

ser = serial.Serial(sys.argv[1], 115200, timeout=1)
ser.open()
ser.write('\x03\x01\x00\x00')
ser.read(4096)
ser.write('\x04\x07')

while 1:
	temp = ser.read(4096)
	f.write(temp)
