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



if __name__ == '__main__':
	filein = open('example2.py','r')
	lib = importing(filein)
	filein.close()
	filein = open('example2.py','r')
	pins = FindPins(filein,lib[-1]['platfrom'])
	filein.close()
	filein = open('example2.py','r')
	code = FindCode(filein,lib,pins)
	for item in lib:
		print item 
	for item in pins:
		print item
	for item in code:
		print item
	filein.close()