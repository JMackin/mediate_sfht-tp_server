import json
import os


class Places:

    def __init__(self, pl_name, mappings='places/mappings'):
        def mk_empty_mappings():
            empty_maps = {
                'server': {},
                'client': {}
            }
            with open('places/mappings', 'w') as mps:
                json.dump(empty_maps, mps)

            print('\nMappings file not found.'
                  '\nPlease make required entries in "places/mappings" before using this class')
            quit()

        def build_index(place_locations_dict):
            place_locations = place_locations_dict.get("place_locations")
            places_index = {}
            for place, loc in place_locations.items():
                print(f"\nplace: {place}\nloc: {loc}\n\n")
                with open(loc, 'r') as floc:
                    read_place_file = floc.readlines()
                    places_index[place] = {i[0].strip(): i[1].strip() for i in
                                           [ii.split(':') for ii in read_place_file]}
            return places_index

        if not os.path.exists(mappings):
            mk_empty_mappings()
        else:
            with open(mappings, 'r') as mps:
                mps_decoded = json.load(mps)
                self.pl_name = pl_name
                self.pl_loc = build_index(mps_decoded)


    def ls_targets_for_place(self):
        return self.pl_loc.get(self.pl_name)

    def target_from_place(self, target):
        return self.pl_loc.get(self.pl_name).get(target)








