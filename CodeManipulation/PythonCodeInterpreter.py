def OpenAndCreateFile(file,name):
	File_out = open('%s' % name, 'w')
	
	code = []


	for item in file:
		File_in = open('%s' % item,'r')
		#...GetInfo...
		#0 find pin or while.
		readline = InFile.readline()
		Libs = FindLibary(readline,bro)
		Pins = FindPins(readline,bro)
		#def 
		#2 call if statements based on type of func
		#3 and libs
		#code.append({'':'import time'})

	return File_out.name 

def FindPins(file,lib):
	i = 0
	line = 'nothing'
	pins = []
	if lib == 'pigpio':
		while(line!=''):
			line = file.readline()
			if '#' in line:
				continue
			if 'set_mode' in line:
				ind = line.index('(')
				if line[ind+2]==',':
					pin = {int(line[ind+1]):line}
				else:
					pin = {int(line[ind+1]+line[ind+2]):line}
				pins.append(pin)
	elif(lib == 'RPi.GPIO'):
		while(line!=''):
			line = file.readline()
			if '#' in line:
				continue
			if 'setup' in line:
				ind = line.index('(')
				if line[ind+2]==',':
					pin = {int(line[ind+1]):line}
				else:
					pin = {int(line[ind+1]+line[ind+2]):line}
				pins.append(pin)
	return pins
def importing(file):
	i = 0
	line = 'nothing'
	libs = []
	while(line!=''):
		line = file.readline()
		if '#' in line:
			continue
		if 'import' in line:
			i+=1
			lib ={i:line}
			libs.append(lib)
			if 'pigpio' in line:
				platform = {'platform':'pigpio'}
			else:
				platform = {'platfrom':'RPi.GPIO'}
	libs.append(platform)
	return libs

