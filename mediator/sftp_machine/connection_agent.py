import mediator.sftp_machine.portals as portals
import os.path
from stat import S_ISDIR, S_ISREG

# Maybe temporary?
import places.place_things.placethings as pthings

serverPlc = pthings.Places('server')
sRoot = serverPlc.target_from_place('ROOT_DIR')
sslnks = serverPlc.target_from_place('SLINKS')

clientPlc = pthings.Places('client')
cRoot = clientPlc.target_from_place('ROOT_DIR')
cDwn_dir = clientPlc.target_from_place('DWNLD_DIR')


class SFTPDoer:

    def __init__(self):
        self.sftp_portal = portals.SftpPortal()
        self.portal_action = self.sftp_portal.get_portal()
        self.curr_dir = os.fspath(sRoot)
        self.portal_action.chdir(self.curr_dir)
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
            self.portal_action.chdir(os.fspath(path))
            self.curr_dir = self.portal_action.getcwd()
            print(f"--> {self.curr_dir}")


    def xls_iter(self, path=None):
        if path is None:
            path = self.curr_dir

        # listdir_iter has parameter 'read-aheads=50'
        # maybe useful for pagination
        return self.portal_action.listdir_iter(path)

    def xls_attr(self, path=None):
        if path is None:
            path = self.curr_dir

        return self.portal_action.listdir_attr(path)

    def xls(self, path=None):
        if path is None:
            path = self.curr_dir

        for file in self.portal_action.listdir_attr(path):
            if S_ISDIR(file.st_mode):
                print(f"{file.filename}/")
            else:
                print(f"{file.filename}")

    def xls_blunt(self, path=None):
        if path is None:
            path = self.curr_dir
        return self.portal_action.listdir(path)

    # Download target to client download folder
    def xget(self, target, dwnld_path=None):
        if dwnld_path is None:
            dwnld_path = self.client_dest_dir

        target_name = target.split('/')[-1]
        dest = f"{dwnld_path}/{target_name}"

        self.portal_action.get(target, localpath=dest)

    # From Paramiko:
    #       ** Copy a remote file (remotepath) from the SFTP server and write to an open file or file-like object **
    def xget_fopen(self, target, file_obj):
        self.portal_action.getfo(target, file_obj)
        return file_obj

    # From Paramiko:
    #       ** Open a file on the remote server. A file-like object is returned. **
    def xfopen(self, target):
        return self.portal_action.open(target, 'r')

    # Make and store a symlink for easy access later, marked w/ given id.
    def xmk_slink(self, target, link_id):

        new_sLink = os.fspath(f"{sRoot}/{self.sSlnks}/{link_id}")

        if os.path.exists(new_sLink):
            print('\nLink w/ that id exists\n')
            return

        if os.path.exists(self.sSlnks):
            self.portal_action.symlink(target, link_id)
        else:
            self.portal_action.mkdir(os.fspath(f"{self.sSlnks}"))
            self.xmk_slink(target, link_id)

    def xread_slink(self, link_id):
        return self.portal_action.readlink(os.fspath(f"{self.sSlnks}/{link_id}"))

    def get_portal_actor(self):
        return self.portal_action



doer = SFTPDoer()

print(doer.xls_blunt())
print(doer.xls_attr())
print(doer.xls())

