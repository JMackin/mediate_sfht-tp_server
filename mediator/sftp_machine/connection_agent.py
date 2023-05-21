import mediator.sftp_machine.portals as portals
import os.path
from stat import S_ISDIR, S_ISREG



class SFTPDoer:

    sftp_portal = portals.SftpPortal()
    portal_action = sftp_portal.get_portal()
    # TODO: Get starting directory from environ or conf file
    curr_dir = os.fspath('/')

    portal_action.chdir(curr_dir)

    def xcwd(self):
        return self.curr_dir

    def xls_iter(self, path: str = curr_dir):
        return self.portal_action.listdir_iter(path)

    def xls_attr(self, path: str = curr_dir):
        return self.portal_action.listdir_attr(path)

    def xls(self, path: str = curr_dir):
        for file in self.portal_action.listdir_attr(path):
            if S_ISDIR(file.st_mode):
                print(f"<dir>{file.filename}")
            else:
                print(f"<dir>{file.filename}")

    def xls_blunt(self, path: str = curr_dir):
        return self.portal_action.listdir(path)

    def get_portal_actor(self):
        return self.portal_action


doer = SFTPDoer()

print(doer.xls_blunt())
print(doer.xls_attr())
print(doer.xls())

