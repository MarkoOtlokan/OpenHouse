import paramiko

def uploadCode(ip, username, password, filename):
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip,port='7055',username=username,password=password)
        ftp = ssh.open_sftp()
        ftp.put(filename, 'remotefile.py')
        stdin, stdout, stderr = ssh.exec_command("python remotefile.py")
        ftp.close()