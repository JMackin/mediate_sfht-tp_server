import os
import paramiko as pmiko
from paramiko.ssh_exception import AuthenticationException, SSHException

import scrts.secret_things.secretThings as secth
# import mediator.mediator.objects.models as models

#TODO impliment security measures and hashing for storing keys on server


# class QueryFiles(models.Media):
#
#     mtype = models.Media.getMType()
#     dest_path = models.Media.get_dir()
#

class SftpPortal:
    class ConnectionBuilder:

        secret = secth.Secrets()

        #TODO key hashing, maybe implementing an secrets manager or database tied to server hardware

        def get_sftp_key(self):

            key_pwd = self.secret.get_keypass('sftp-s')
            keyfile = os.fspath(self.secret.get_keyloc('sftp-s'))

            with open(keyfile) as key:
                pk = pmiko.ed25519key.Ed25519Key.from_private_key(key, password=key_pwd)

            return pk

        def build_ssh_client(self):

            sftp_key = self.get_sftp_key()
            username = self.secret.get_username('sftp-user')
            host_ip = self.secret.get_host_ip('sftp-serv')
            host_port = int(self.secret.get_host_port('sftp-serv'))

            ssh_conn = pmiko.client.SSHClient()
            ssh_conn.set_missing_host_key_policy(pmiko.client.AutoAddPolicy())

            try:
                ssh_conn.connect(hostname=host_ip, port=host_port, username=username, pkey=sftp_key)
            except SSHException as auth_except:

                print(f"Failed to establish connection.\n \
                        Parameters used:\n \
                        \thost: {host_ip}\n \
                        \tport: {host_port}\n \
                        \tusername: {username}\n \
                        \tpkey: \n \
                        \t - key: {os.fspath(self.secret.get_keyloc('sftp-s'))}\n \
                        \t - pass: {os.fspath(self.secret.key_pwd.get('sftp-s'))}\n \
                       ")
                print(f"{auth_except.__str__()}")
                return None

            return ssh_conn

        def sftp_portal(self):

            ssh_client = self.build_ssh_client()

            return ssh_client.open_sftp()

    conn_builder = ConnectionBuilder()
    portal = conn_builder.sftp_portal()
    channel_id = portal.get_channel()


    def get_portal(self):
        return self.portal

    def get_chanId(self):
        return self.channel_id

    def is_open(self):
        return self.portal.get_channel().active

    def ready_to_read(self):
        return self.portal.get_channel().recv_ready()

    def __init__(self):
        self.portal = self.conn_builder.sftp_portal()
        self.channel_id = self.portal.get_channel().get_id()

    def __del__(self):
        if self.portal.get_channel().active:
            self.portal.close()

    def __delete__(self, portal):
        if portal.isinstance():
            if self.portal.get_channel().active:
                self.portal.close()

