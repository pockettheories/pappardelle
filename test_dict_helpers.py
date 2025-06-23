import sys
import unittest

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