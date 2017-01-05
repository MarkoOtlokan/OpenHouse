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

def GenerateIfStatement():
	pass

def CheckForPinsMathcing():
	pass
def importing(file):
	i = 0
	line = 'nothing'
	libs = []
	while(line!=''):
		line = file.readline()
		if '#' in line:
			b = 0
			for item in line:
				if item == '#':
					break
				else:
					b+=1
			line1 = line[:b]
		else:
			line1 = line
		if 'import' in line1:
			i+=1
			lib ={i:line1}
			libs.append(lib)
			if 'pigpio' in line1:
				platform = {'platform':'pigpio'}
			else:
				platform = {'platfrom':'RPi.GPIO'}
	libs.append(platform)
	return libs

def FindPins(file,lib):
	i = 0
	line = 'nothing'
	pins = []
	if lib == 'pigpio':
		while(line!=''):
			line = file.readline()
			if '#' in line:
				b = 0
				for item in line:
					if item == '#':
						break
					else:
						b+=1
				line1 = line[:b]
			else:
				line1 = line
			if 'set_mode' in line1:
				ind = line1.index('(')
				if line1[ind+2]==',':
					pin = {int(line1[ind+1]):line1}
				else:
					pin = {int(line1[ind+1]+line1[ind+2]):line1}
				pins.append(pin)
	elif(lib == 'RPi.GPIO'):
		while(line!=''):
			line = file.readline()
			if '#' in line:
				b = 0
				for item in line:
					if item == '#':
						break
					else:
						b+=1
				line1 = line[:b]
			else:
				line1 = line
			if 'setup' in line1:
				ind = line1.index('(')
				if line1[ind+2]==',':
					pin = {int(line1[ind+1]):line1}
				else:
					pin = {line1[ind+1]+line1[ind+2]:line1}
				pins.append(pin)
	return pins

def FindCode(file,lib,pins):
	line = 'nothing'
	code = []
	i = 0
	while(line != ''):
		line = file.readline()
		if '#' in line:
			b = 0
			for item in line:
				if item == '#':
					break
				else:
					b+=1
			line1 = line[:b]
		else:
			line1 = line
		for item in range(len(lib)-1):
			x = True
			if(line1 == lib[item].values()[0]):
				x = False
				break
			else:
				pass
		if(x == True):
			for item in range(len(pins)-1):
				if(line1 == pins[item].values()[0]):
					x = False
					break
				else:
					pass
		if(x == True):
			cod = {i:line1}
			code.append(cod)
		i+=1	
	return code