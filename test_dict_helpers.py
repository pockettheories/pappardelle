import sys
import unittest
import json
from pappardelle import dict_helpers

sys.path.append('pappardelle')  # Include the subdir in the PythonPath

class TestDictHelpers(unittest.TestCase):
    def test_make_set_dict_path(self):
        init_dict_1 = {}
        cities_in_ka = ['coorg', 'hampi', 'gokarna', 'bijapur', 'chikmaglur']
        dict_helpers.make_dict_path(init_dict_1, ['India', 'Karnataka'])

        assert(
            'India' in init_dict_1 and
            'Karnataka' in init_dict_1['India']
        )

        init_dict_1['India']['Karnataka'] = cities_in_ka

        init_dict_2 = {}
        dict_helpers.set_dict_path(init_dict_2, ['India', 'Karnataka'], cities_in_ka)

        assert(
            'India' in init_dict_1 and
            'Karnataka' in init_dict_1['India']
        )

        assert(len(init_dict_1['India']['Karnataka']) == len(cities_in_ka))

    def test_get_dict_path(self):
        test_dict1 = {
            'Me': 'Nitin',
            'Parents': {
                'Dad': 'Narsing',
                'Mom': 'Nita',
            }
        }
        assert(dict_helpers.get_dict_path(test_dict1, ['Parents', 'Mom']) == 'Nita')
        assert (dict_helpers.get_dict_path(test_dict1, ['Me']) == 'Nitin')
        assert (dict_helpers.get_dict_path(test_dict1, ['GrandKids']) is None)

    def test_deep_copy_dict_no_overwrite(self):
        src_dict1 = {
            'India': {
                'Telangana': {
                    'Soan': '19.0054549107483, 78.3784781015872',
                    'Gamjal': '19.019827951385533, 78.36518013572389'
                }
            }
        }

        tpl_dest_dict1 = {
            'UAE': {
                'Dubai': '25.18506895343312, 55.28510706928182'
            },
            'India': {
                'Telangana': {
                    'Soan': 'MANDATORY VISIT',
                    'Hyderabad': '17.416212090368877, 78.45678200830396'
                }
            }
        }

        dest_dict1 = json.loads(json.dumps(tpl_dest_dict1))
        dest_dict2 = json.loads(json.dumps(tpl_dest_dict1))

        dict_helpers.deep_copy_dict_no_overwrite(src_dict1, dest_dict1, False)
        dict_helpers.deep_copy_dict_no_overwrite(src_dict1, dest_dict2, True)

        assert(dest_dict1['UAE']['Dubai'] == '25.18506895343312, 55.28510706928182')
        assert(dest_dict1['India']['Telangana']['Soan'] == 'MANDATORY VISIT')
        assert(dest_dict1['India']['Telangana']['Hyderabad'] == '17.416212090368877, 78.45678200830396')
        assert(dest_dict1['India']['Telangana']['Gamjal'] == '19.019827951385533, 78.36518013572389')

        assert(dest_dict2['UAE']['Dubai'] == '25.18506895343312, 55.28510706928182')
        assert(dest_dict2['India']['Telangana']['Soan'] == '19.0054549107483, 78.3784781015872')
        assert(dest_dict2['India']['Telangana']['Hyderabad'] == '17.416212090368877, 78.45678200830396')
        assert(dest_dict2['India']['Telangana']['Gamjal'] == '19.019827951385533, 78.36518013572389')
