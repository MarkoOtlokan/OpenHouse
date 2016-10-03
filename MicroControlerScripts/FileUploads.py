import paramiko

def uploadCode(ip, port, username, password, filename):
	ssh = paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	ssh.connect(ip,port=port,username=username,password=password)
	ftp = ssh.open_sftp()
	ftp.put('RassperrypiCodes/%s/%s' % (username,filename) , 'remotefile.py')
	stdin, stdout, stderr = ssh.exec_command("python remotefile.py")
	ftp.close()

def uploadArduinocode(ip, port, username, password, filename, arduinoBoard):
	ssh = paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	ssh.connect(ip,port=port,username=username,password=password)
	stdin, stdout, stderr = ssh.exec_command("pip install -U platformio")
	stdin, stdout, stderr = ssh.exec_command("platformio init --board %s" % arduinoBoard )
	ftp = ssh.open_sftp()
	ftp.put('src/main.c','RassperrypiCodes/Functions/%s' % filename)
	stdin, stdout, stderr = ssh.exec_command("platformio run -t upload")

def arduinoToSleep(ip, port, username, password, filename, arduinoBoard):
	ssh = paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	ssh.connect(ip,port=port,username=username,password=password)
	stdin, stdout, stderr = ssh.exec_command("pip install -U platformio")
	stdin, stdout, stderr = ssh.exec_command("platformio init --board %s" % arduinoBoard )
	ftp = ssh.open_sftp()
	ftp.put('src/main.c','sleep.c')
	stdin, stdout, stderr = ssh.exec_command("platformio run -t upload")

