from typing import Optional

from paramiko.client import SSHClient, AutoAddPolicy
from paramiko.rsakey import RSAKey
from paramiko.sftp_client import SFTPClient


class SshConnection:
    """远程登录服务器"""
    def __init__(self) -> None:
        self.ssh_client = SSHClient()
        # AutoAddPolicy策略会自动把登录信息保存在本地
        self.ssh_client.set_missing_host_key_policy(AutoAddPolicy())
        self.sftp: Optional[SFTPClient] = None

    def connect_by_password(self, ip: str, pwd: str, port: int = 22, username: str = "root", timeout: float = 10):
        """ssh连接服务器, 通过用户名密码登录"""
        self.ssh_client.connect(hostname=ip, port=port, username=username, password=pwd, timeout=timeout)
        transport = self.ssh_client.get_transport()
        self.sftp = SFTPClient.from_transport(transport)

    def connect_by_pkey(self, ip: str, pkey_filename: str = r"C:\Users\Administrator\.ssh\id_rsa",
                        pkey_pwd: Optional[str] = None, port: int = 22, username: str = "root", timeout: float = 10):
        """
        ssh连接服务器, 通过密钥连接登录
        id_rsa: 是私钥(客户端使用)，id_rsa.pub 这个是公钥(服务器使用); 只需要把私钥复制到本地主机路径: C:\\Users\\Administrator\\.ssh\\id_rsa
        pkey_filename: 密钥的文件路径, 本地主机默认路径: C:\\Users\\Administrator\\.ssh\\id_rsa
        pkey_pwd: 如果密钥中输入了密码, pkey_pwd需要填写密码, 否者为 None
        """
        pkey = RSAKey.from_private_key_file(filename=pkey_filename, password=pkey_pwd)
        self.ssh_client.connect(hostname=ip, port=port, username=username, pkey=pkey, timeout=timeout)
        transport = self.ssh_client.get_transport()
        self.sftp = SFTPClient.from_transport(transport)

    def push(self, local_file: str, remote_file: str):
        """
        sfpt上传文件
        文件存在就覆盖, 不存在就创建
        文件目录不存在就报错
        """
        self.sftp.put(local_file, remote_file)

    def pull(self, remote_file: str, local_file: str):
        """
        sftp下载文件
        文件存在就覆盖, 不存在就创建
        文件目录不存在就报错
        """
        self.sftp.get(remote_file, local_file)

    def exec_cmd(self, cmd: str, timeout=10) -> str:
        """执行shell指令, 执行指令出错返回错误信息, 执行指令正确返回正确信息"""
        _, stdout, stderr = self.ssh_client.exec_command(cmd, timeout=timeout)
        usual_msg = stdout.read().decode().strip()
        err_msg = stderr.read().decode().strip()
        if err_msg:
            return err_msg
        return usual_msg

    def close(self):
        """关闭ssh连接"""
        self.ssh_client.close()


