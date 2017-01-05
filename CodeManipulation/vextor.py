import paramiko
import time
vex = time.time()
ssh = paramiko.SSHClient()
print time.time()-vex
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
print time.time()-vex
ssh.connect('192.168.1.4',port=8000,username='root',password='veljko')
print time.time()-vex
ftp = ssh.open_sftp()
print time.time()-vex
stdin, stdout, stderr = ssh.exec_command("ls -l")
print time.time()-vex
print stdout.read()
print time.time()-vex
ftp.close()
print time.time()-vex