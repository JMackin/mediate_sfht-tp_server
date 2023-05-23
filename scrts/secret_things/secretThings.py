import os.path
import json


class Secrets:

    def __init__(self, mappings='scrts/mappings'):
        def mk_empty_mappings():
            empty_maps = {
                'key_loc:': {},
                'key_pwd': {},
                'users': {},
                'hosts': {}
            }
            with open('scrts/mappings', 'w') as mps:
                json.dump(empty_maps, mps)

            print('\nMappings file not found.'
                  '\nPlease make required entries in "scrts/mappings" before using this class')
            quit()

        if not os.path.exists(mappings):
            mk_empty_mappings()
        else:
            with open(mappings, 'r') as mps:
                mps_decoded = json.load(mps)
                self.key_loc = mps_decoded.get('key_loc')
                self.key_pwd = mps_decoded.get('key_pwd')
                self.users = mps_decoded.get('users')
                self.hosts = mps_decoded.get('hosts')

    def get_keyloc(self, keyid):
        return self.key_loc.get(keyid)

    def get_keyid_list(self):
        return [i for i in self.key_loc.keys()]

    def list_keys(self):
        for i in self.key_loc.keys():
            print(i)

    def get_keypass(self, keyid):
        with open(self.key_pwd.get(keyid), 'r') as ks:
            return ks.read()

    def get_secret(self, keyid):
        with open(self.key_loc.get(keyid), 'r') as ks:
            return ks.read()

    def get_username(self, userid):
        with open(self.users.get(userid), 'r') as un:
            return un.read()

    def list_users(self):
        for i in self.users.keys():
            print(i)

    def get_userid_list(self):
        return [i for i in self.users.keys()]

    def get_host(self, hostid):
        with open(self.hosts.get(hostid), 'r') as hst:
            return hst.read().splitlines()

    def get_host_ip(self, hostid):
        return self.get_host(hostid)[0].split(':')[1].strip()

    def get_host_port(self, hostid):
        return self.get_host(hostid)[1].split(':')[1].strip()


