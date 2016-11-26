import paramiko
import time

def uploadCode(ip, username, password, filename):
	ssh = paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	ssh.connect(ip,port=22,username=username,password=password)
	ftp = ssh.open_sftp()
	ftp.put('RassperrypiCodes/%s/%s' % (username,filename) , 'remotefile.py')
	stdin, stdout, stderr = ssh.exec_command("python remotefile.py")
	ftp.close()

def uploadArduinocode(ip, username, password, filename, arduinoBoard):
	ssh = paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	ssh.connect(ip,port=22,username=username,password=password)
	stdin, stdout, stderr = ssh.exec_command("pip install -U platformio")
	time.sleep(15)
	stdin, stdout, stderr = ssh.exec_command("platformio init --board %s" % arduinoBoard )
	time.sleep(3)
	ftp = ssh.open_sftp()
	ftp.put('src/main.c','RassperrypiCodes/Functions/%s' % filename)
	stdin, stdout, stderr = ssh.exec_command("platformio run -t upload")
	time.sleep(70)

def arduinoToSleep(ip, username, password, arduinoBoard):
	ssh = paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	ssh.connect(ip,username=username,password=password)
	stdin, stdout, stderr = ssh.exec_command("pip install -U platformio")
	time.sleep(15)
	stdin, stdout, stderr = ssh.exec_command("platformio init --board %s" % arduinoBoard )
	time.sleep(3)
	ftp = ssh.open_sftp()
	ftp.put('sleep.c','src/main.c')
	stdin, stdout, stderr = ssh.exec_command("platformio run -t upload")
	time.sleep(70)

if __name__ == "__main__":
	arduinoToSleep('localhost','ssh1','kerlaje1234','nanoatmega328')