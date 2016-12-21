filein = open('example3.py','r')

def importing(file):
	i = 0
	line = 'nothing'
	libs = []
	while(line!=''):
		line = file.readline()
		if '#' in line:
			continue
		if 'import' in line:
			print line
			i+=1
			lib ={i:line}
			libs.append(lib)
			if 'pigpio' in line:
				platform = {'platform':'pigpio'}
			else:
				platform = {'platfrom':'RPi.GPIO'}
	libs.append(platform)
	print libs
	return libs

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
					print line[ind+1]
					pin = {int(line[ind+1]):line}
				else:
					print line[ind+1]+line[ind+2]
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

def FindCode(file,lib,pins):
	line = 'nothing'
	print 'a'
	code = []
	i = 0
	while(line != ''):
		line = file.readline()
		if '#' in line:
			h = 0
			for item in line:
				if(item == '#'):
					break
				else:
					h+=1
			line = line[:h]
			print line
		for item in range(len(lib)-1):
			x = True
			if(line == lib[item].values()[0]):
				x = False
				break
			else:
				pass
		if(x == True):
			cod = {i:line}
			code.append(cod)
		i+=1	
		print i
	for item in code:
		print item 




if __name__ == '__main__':
	vex = importing(filein)
	filein.close()
	#FindPins(filein,'RPi.GPIO')
	filein = open('example3.py','r')
	FindCode(filein,vex,'123')