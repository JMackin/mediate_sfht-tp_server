import os.path
from stat import S_ISDIR

# Maybe temporary?
import places.place_things.placeThings as pthings
from . import portals as portals

plc = pthings.Places()
serverPlc = plc.get_place_loc('server')
sRoot = plc.get_target_fromPlace('ROOT_DIR', 'server')
sslnks = plc.get_target_fromPlace('SLINKS', 'server')

clientPlc = plc.get_place_loc('client')
cRoot = plc.get_target_fromPlace('ROOT_DIR', 'client')
cDwn_dir = plc.get_target_fromPlace('DWNLD_DIR', 'client')


# TODO: Open new channels for separate users over single transport session
# From Paramiko - paramiko.transport.Transport:
#       ** Multiple channels can be multiplexed across a single session **


class SFTPDoer:

    def __init__(self, transport: portals.SftpPortal):
        self.sftp_portal = transport.sftp_portal()
        # self.portal_action = self.sftp_portal.get_portal()
        self.curr_dir = os.fspath(sRoot)
        self.sftp_portal.chdir(self.curr_dir)
        self.client_dest_dir = os.fspath(cDwn_dir)
        self.sSlnks = os.fspath(sslnks)
    # TODO: Get starting directory from environ or conf file

    # Variable for destination folder for downloaded folders.

    def xcwd(self):
        return self.curr_dir

    def xch_dir(self, path=None):
        if path is None:
            print('No such path. No action performed')
            return
        else:
            print(self.curr_dir)
            self.sftp_portal.chdir(os.fspath(path))
            self.curr_dir = self.sftp_portal.getcwd()
            print(f"--> {self.curr_dir}")


    def xls_iter(self, path=None):
        if path is None:
            path = self.curr_dir

        # listdir_iter has parameter 'read-aheads=50'
        # maybe useful for pagination
        return self.sftp_portal.listdir_iter(path)

    def xls_attr(self, path=None):
        if path is None:
            path = self.curr_dir

        return self.sftp_portal.listdir_attr(path)

    def xls(self, path=None):
        if path is None:
            path = self.curr_dir

        for file in self.sftp_portal.listdir_attr(path):
            if S_ISDIR(file.st_mode):
                print(f"{file.filename}/")
            else:
                print(f"{file.filename}")

    def xls_blunt(self, path=None):
        if path is None:
            path = self.curr_dir
        return self.sftp_portal.listdir(path)

    # Download target to client download folder
    def xget(self, target, dwnld_path=None):
        if dwnld_path is None:
            dwnld_path = self.client_dest_dir

        target_name = target.split('/')[-1]
        dest = f"{dwnld_path}/{target_name}"

        self.sftp_portal.get(target, localpath=dest)

    # From Paramiko:
    #       ** Copy a remote file (remotepath) from the SFTP server and write to an open file or file-like object **
    def xget_fopen(self, target, file_obj):
        self.sftp_portal.getfo(target, file_obj)
        return file_obj

    # From Paramiko:
    #       ** Open a file on the remote server. A file-like object is returned. **
    def xfopen(self, target):
        return self.sftp_portal.open(target, 'r')

    # Make and store a symlink for easy access later, marked w/ given id.
    def xmk_slink(self, target, link_id):

        new_sLink = os.fspath(f"{sRoot}/{self.sSlnks}/{link_id}")

        if os.path.exists(new_sLink):
            print('\nLink w/ that id exists\n')
            return

        if os.path.exists(self.sSlnks):
            self.sftp_portal.symlink(target, link_id)
        else:
            self.sftp_portal.mkdir(os.fspath(f"{self.sSlnks}"))
            self.xmk_slink(target, link_id)

    def xread_slink(self, link_id):
        return self.sftp_portal.readlink(os.fspath(f"{self.sSlnks}/{link_id}"))

    def get_portal_actor(self):
        return self.sftp_portal

    def __del__(self):
        self.get_portal_actor().get_channel().close()


