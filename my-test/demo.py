import paramiko
from paramiko.client import AutoAddPolicy

if __name__ == '__main__':
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(AutoAddPolicy)
    ssh.connect(hostname="192.168.56.201", username="root", password="1234", timeout=10)
    stdin, stdout, stderr = ssh.exec_command(r"cat 10.txt", timeout=10)
    print(stdout.read())
    ftp = paramiko.Transport(("192.168.56.201", 22))
    ftp.connect()
    ssh.close()
