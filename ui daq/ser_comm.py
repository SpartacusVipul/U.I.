import serial
import numpy as np
import time
import matplotlib.pyplot as plt
from ip_func import *

ser = serial.Serial()

#serial setup

ser.port = '/dev/ttyUSB0'
#ser.baudrate = 115200
ser.baudrate = 1000000
ser.bytesize = serial.EIGHTBITS
ser.parity = serial.PARITY_NONE
ser.stopbits = serial.STOPBITS_ONE
ser.timeout = 1


#connect
try:
	ser.open()

except:
	print "cannot open serial port"

#default values
# global buf		#number of samples in one window
# global now		#number of windows sampled
# global err_flag
# global data

buf = 1000;		#number of samples in one window
now = 128;		#number of windows sampled
err_flag = 0
data = ''
ip = ''
def ser_comm_main(ser,buf,now,data,ip):
	print "****************************************"
	if(err_flag):
		time.sleep(2)
		print ser.read(50)
	else:
		time.sleep(2)
		flush(ser)
		n = ser.inWaiting()
		ser.read(n)
	print "****************************************"
	# ip=raw_input("Type your action (h for help)  ")
	# global ip

	if(ser.inWaiting()):
		print "random data might be present"
		setup_delay()

	elif(ip=='i'):
		#get configuration information
		print "getting current configuration"
		[buf,now] = get_confg(ser)
		print "buffer size  = ", buf
		print "# window avg = ", now
		print "DONE"

	elif(ip=='o'):
		#set configutaion
		print "setting configuration"
		set_confg(ser)
		time.sleep(2)
		[buf,now] = get_confg(ser)
		print "DONE"

	elif(ip=='h'):
		#print help
		print help_array

	elif(ip=='t'):
		#led blink
		print "twiddle LEDS"
		while(not ser.write('t')):
			pass
		print "DONE"

	elif(ip=='a'):
		#asynchronus sampling only one window
		print "asynchronus sampling"
		while(not ser.write('a')):
			pass
		print "DONE"
		time.sleep(0.02)#maximum time needed for sampling

	elif(ip=='s'):	
		#synchronus sampling only one window
		print "synchronus sampling"
		while(not ser.write('s')):
			pass
		print "DONE"
		time.sleep(0.02)#maximum time needed for sampling

	elif(ip=='d'):
		#synchronus sampling with decimal value transfer
		print "synchronus sampling with decimal value transfer"
		print "windows # = ", now
		print "please Wait"
		del data
		#decimal values in serial communication
		data = average_sample1(ser,buf,now);
		print "DONE"

	elif(ip=='x'):
		#synchronus sampling with hexa decimal value transfer
		print "synchronus sampling with HEXA-decimal value transfer"
		print "windows # = ", now
		print "please Wait"
		del data
		#HEXA-decimal values in serial communication
		data = average_sample2(ser,buf,now);
		print "DONE"

	elif(ip=='g'):
		#plot graph
		print "plotting graph of data"
		try:
			plot_data(data)
		except:
			print "error in data"
		print "DONE"

	elif(ip=='f1'):
		#plot butter
		BW = float(raw_input('BandWidth in kHz : '))
		N  =   int(raw_input('Order            : '))
		plot_filt_data(data,BW,N)

	elif(ip=='f2'):
		#plot kaiser
		BW = float(raw_input('BandWidth in kHz : '))
		N  =   int(raw_input('attenuation      : '))
		plot_filt_kaiser(data,BW,N)

if ser.isOpen():
	print "connection Established"
	try:
		ser.flushInput()
		ser.flushOutput()
		setup_delay(ser)
		print ser.read(ser.inWaiting())
		[buf,now] = get_confg(ser)
		# while(1):
			# ser_comm_main(ser,buf,now,data,ip)
			# print "****************************************"
			# if(err_flag):
			# 	time.sleep(2)
			# 	print ser.read(50)
			# else:
			# 	time.sleep(2)
			# 	flush(ser)
			# 	n = ser.inWaiting()
			# 	ser.read(n)
			# print "****************************************"
			# ip=raw_input("Type your action (h for help)  ")

			# if(ser.inWaiting()):
			# 	print "random data might be present"
			# 	setup_delay()

			# elif(ip=='i'):
			# 	#get configuration information
			# 	print "getting current configuration"
			# 	[buf,now] = get_confg(ser)
			# 	print "buffer size  = ", buf
			# 	print "# window avg = ", now
			# 	print "DONE"

			# elif(ip=='o'):
			# 	#set configutaion
			# 	print "setting configuration"
			# 	set_confg(ser)
			# 	time.sleep(2)
			# 	[buf,now] = get_confg(ser)
			# 	print "DONE"

			# elif(ip=='h'):
			# 	#print help
			# 	print help_array

			# elif(ip=='t'):
			# 	#led blink
			# 	print "twiddle LEDS"
			# 	while(not ser.write('t')):
			# 		pass
			# 	print "DONE"

			# elif(ip=='a'):
			# 	#asynchronus sampling only one window
			# 	print "asynchronus sampling"
			# 	while(not ser.write('a')):
			# 		pass
			# 	print "DONE"
			# 	time.sleep(0.02)#maximum time needed for sampling

			# elif(ip=='s'):	
			# 	#synchronus sampling only one window
			# 	print "synchronus sampling"
			# 	while(not ser.write('s')):
			# 		pass
			# 	print "DONE"
			# 	time.sleep(0.02)#maximum time needed for sampling
			
			# elif(ip=='d'):
			# 	#synchronus sampling with decimal value transfer
			# 	print "synchronus sampling with decimal value transfer"
			# 	print "windows # = ", now
			# 	print "please Wait"
			# 	del data
			# 	#decimal values in serial communication
			# 	data = average_sample1(ser,buf,now);
			# 	print "DONE"

			# elif(ip=='x'):
			# 	#synchronus sampling with hexa decimal value transfer
			# 	print "synchronus sampling with HEXA-decimal value transfer"
			# 	print "windows # = ", now
			# 	print "please Wait"
			# 	del data
			# 	#HEXA-decimal values in serial communication
			# 	data = average_sample2(ser,buf,now);
			# 	print "DONE"

			# elif(ip=='g'):
			# 	#plot graph
			# 	print "plotting graph of data"
			# 	try:
			# 		plot_data(data)
			# 	except:
			# 		print "error in data"
			# 	print "DONE"

			# elif(ip=='f1'):
			# 	#plot butter
			# 	BW = float(raw_input('BandWidth in kHz : '))
			# 	N  =   int(raw_input('Order            : '))
			# 	plot_filt_data(data,BW,N)

			# elif(ip=='f2'):
			# 	#plot kaiser
			# 	BW = float(raw_input('BandWidth in kHz : '))
			# 	N  =   int(raw_input('attenuation      : '))
			# 	plot_filt_kaiser(data,BW,N)


	except:
		print "closing forcefully: Error Occured"
		ser.close()