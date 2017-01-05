filein = open('vextor.py','r')
line = 'nothing'
fileout = open('vextor1.py','w')
while(line != ''):
	line = filein.readline()
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
	fileout.write(line1+'\n')