def voltage_ripple(VAC, Iav, C):
	VDC = 0
	Vrip = 0
	Vrip_per = 0
	print('You enter VAC = %fV'%VAC)
	print ('Current of load = %fA'%Iav)
	print('Capacitance = %fuF'%C)
	VDC = VAC*1.414-1.2
	print('Maximum voltage after full bridge rectifier = %fV'%VDC)
	Vrip = Iav/(2*C*(10**-6)*50)
	print('Voltage ripple on load = %fV'%Vrip)
	Vrip_per = Vrip/VDC*100
	print('Voltage ripple on load = %f%%' %Vrip_per)
	print('Percent of ripple is', end=' ') 
	if Vrip_per <= 1:
		print('exelent')
	elif Vrip_per <= 2:
		print('good')
	elif Vrip_per <= 5:
		print('not bad')
	elif Vrip_per <= 10:
		print('normal')
	elif Vrip_per <= 20:
		print('very bad')
	else:
		print('it`s won`t work correctly')
	return Vrip
