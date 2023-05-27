import json
import os

# mappings = str(os.getenv('self.plcs_mappings'))
# TODO: fix environment variables issues

class Places:

    def __init__(self):

        self.plcs_mappings = str(os.getenv('PLCS_MAPPINGS'))
        print(self.plcs_mappings)
        def mk_empty_mappings():
            empty_maps = {
                "place_locations":
                {
                    "client": "",
                    "server": ""
                },
            }

            with open(self.plcs_mappings, 'w') as mps:
                json.dump(empty_maps, mps)

            print('\nMappings file not found.'
                  '\nPlease make required entries in "plcs/mappings" before using this class')
            quit()

        if not os.path.exists(self.plcs_mappings):
            mk_empty_mappings()
        else:
            print(self.plcs_mappings)
            with open(self.plcs_mappings, 'r') as mps:
                mps_decoded = json.load(mps)
                print(mps_decoded)
                print(mps.__str__())
                self.key_plcs = mps_decoded['place_locations']
                self.key_srvr = mps_decoded.get('place_locations')["server"]
                self.key_client = mps_decoded.get('place_locations')["client"]

    def get_place_loc(self, keyid: str = 'server' or 'client'):

        if keyid == 'server':

            key_obj = self.key_srvr
        else:
            key_obj = self.key_client

        with open(self.plcs_mappings, 'r') as mps:
            mps_decoded = json.load(mps)
            return mps_decoded

    # TODO: clean this up
    def get_target_fromPlace(self, target, place: str = 'server' or 'client'):

        if place == 'server':
            key_obj = self.key_srvr
        else:
            key_obj = self.key_client
        print(key_obj)
        with open(key_obj, 'r') as targets:
            open_targets = targets.readlines()

            for i in open_targets:
                ea = i.split(':')[0]
                if ea == target:
                    return ea

    def get_places_list(self):
        return [i for i in self.key_plcs]

    # def list_keys(self):
    #     for i in self.key_srvr.keys():
    #         print(i)
    #
    # def get_keypass(self, keyid):
    #     with open(self.key_client.get(keyid), 'r') as ks:
    #         return ks.read()
    #
    # def get_secret(self, keyid):
    #     with open(self.key_srvr.get(keyid), 'r') as ks:
    #         return ks.read()
    #
    # def get_username(self, userid):
    #     with open(self.users.get(userid), 'r') as un:
    #         return un.read()
    #
    # def list_users(self):
    #     for i in self.users.keys():
    #         print(i)
    #
    # def get_userid_list(self):
    #     return [i for i in self.users.keys()]
    #
    # def get_host(self, hostid):
    #     with open(self.hosts.get(hostid), 'r') as hst:
    #         return hst.read().splitlines()
    #
    # def get_host_ip(self, hostid):
    #     return self.get_host(hostid)[0].split(':')[1].strip()
    #
    # def get_host_port(self, hostid):
    #     return self.get_host(hostid)[1].split(':')[1].strip()


