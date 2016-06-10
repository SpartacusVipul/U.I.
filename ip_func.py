import time
import numpy as np
import matplotlib.pyplot as plt


help_array = """
h   :    help
p   :    plot_data
a   :    asynchronus sampling
s   :    synchronus sampling
r   :    restore ADC buffer
t   :    twiddle LEDs
i   :    get configuration
o   :    set configuration
d   :    synchronus multiple windows sampling with decimal value transfer
x   :    synchronus multiple windows sampling with   HEX   value transfer
"""

#flushes serial input and output of handle
def flush(ser):
	try:
		ser.flushInput()
		ser.flushOutput()
	except:
		print "error in flush"
def read_ser_large(ser,read_char):
	# flush(ser)

	data = ''
	k = np.zeros(48000) #number of samples in one cycle of while loop
	ser.write(read_char)
	while(not ser.inWaiting()):
		pass
	tic=time.time()
	time.sleep(0.001)
	i=0
	n = ser.inWaiting()
	while(n):
		k[i] = n
		data=data+ser.read(n)
		i=i+1;
		time.sleep(0.005)
		n = ser.inWaiting()
	tic = time.time() - tic
	
	return [data_int[0:len(data)],tic,k,data]

def setup_delay(ser):
	#needed to make sure mc does not have any unfinished data
	# transfer left
	flush(ser);
	tic = time.time()
	print "wait for few seconds"
	while(1):
		n = ser.inWaiting()
		while(n):
			tic = time.time()
			ser.read(n)
			n = ser.inWaiting()
		if((time.time()-tic)>5):
			break
	print "thank you for waiting"

def average_sample1(ser,buf,now):
	#expects decimal characters in serial comm
	k = np.zeros(48000)
	i = 0
	rec_noc = 0
	data = ''
	#maximum characters expected
	max_noc = buf*now*5 + 17

	ser.write('d')
	n = ser.inWaiting()

	while(1):
		if(n):
			data = data + ser.read(n)
		time.sleep(0.01)
		n = ser.inWaiting()
		k[i] = n
		if(n):
			rec_noc = rec_noc + n
			#print i,rec_noc,n
			if(rec_noc==max_noc):
				break
			i+=1

	print "DATA aquisation done || Averaging..."
	
	data1 = data[3:]			#remove initial characters
	data2 = np.zeros(buf*now)

	#convert to integer
	for i in range(0,buf*now):
		data2[i] = int(data1[i*5:i*5+4])

	#find average of all the data obtained
	avgSig = np.zeros(buf)
	for i in range(0,now):
		avgSig = avgSig + data2[i*buf:(i+1)*buf]
	avgSig = avgSig/float(now)

	return avgSig

def average_sample2(ser,buf,now):
	#expects hexadecimal characters in serial comm
	k = np.zeros(48000)
	i = 0
	rec_noc = 0
	data = ''
	#maximum characters expected
	max_noc = buf*now*2 + 17

	ser.write('h')
	n = ser.inWaiting()

	while(1):
		if(n):
			data = data + ser.read(n)
		time.sleep(0.01)
		n = ser.inWaiting()
		k[i] = n
		if(n):
			rec_noc = rec_noc + n
			# print i,rec_noc,n
			if(rec_noc==max_noc):
				break
			i+=1
	data1 = data[3:]			#remove initial characters
	data2 = np.zeros(buf*now)

	print "DATA aquisation done || Averaging..."
	
	#convert to integer
	for i in range(0,buf*now):
		data2[i] = int(str(int(data1[2*i].encode('hex'),16))+str(int(data1[2*i+1].encode('hex'),16)))		

	#find the average
	avgSig = np.zeros(buf)
	for i in range(0,now):
		avgSig = avgSig + data2[i*buf:(i+1)*buf]

	avgSig = avgSig/float(now)

	return avgSig

def get_confg(ser):
	ser.read(ser.inWaiting())
	ser.write('i')
	time.sleep(0.01)
	info = ser.read(ser.inWaiting())
	buf = int(info[3:11])
	now = int(info[11:15])
	return [buf,now]

def set_confg(ser):
	buf = raw_input("choose buffer size: 1->100,2->1000,3->10000(F),4->48000(F): ")
	while(not ser.write('b')):
		pass
	time.sleep(0.01)
	while(not ser.write(buf)):
		pass
	time.sleep(0.01)
	ser.read(ser.inWaiting())

	now = raw_input("choose # of avgs : 1->16,2->64,3->128,4->256,5->512,6->1024: ")
	while(not ser.write('q')):
		pass
	time.sleep(0.01)
	while(not ser.write(now)):
		pass
	time.sleep(0.01)
	ser.read(ser.inWaiting())

def plot_data(data):
	time = np.arange(len(data))/3.6e6
	plt.figure()
	plt.plot(time,data)
	plt.show()

def plot_filt_data(data,BW,N=4):
	ws = BW*1e3/3.6e6*2
	[b,a] = signal.butter(N,ws,'low')
	data_filt = signal.filtfilt(b,a,data)
	time = np.arange(len(data_filt))/3.6e6
	
	plt.figure()
	plt.plot(time,data_filt)
	plt.show()

def plot_filt_kaiser(data,BW,att):
	ws = BW*1e3*2/3.6e6
	[n,beta] = signal.kaiserord(att,ws)
	win = signal.kaiser(n,beta)
	data_filt = signal.convolve(data,win)
	time = np.arange(len(data_filt))/3.6e6
	plt.figure()
	plt.plot(time,data_filt)
	plt.show()
