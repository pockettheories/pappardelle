import sys

from pappardelle import compare_lists
from pappardelle import lookup_lists
import json
import unittest


sys.path.append('pappardelle')  # Include the subdir in the PythonPath


class TestPappardelle(unittest.TestCase):
    def test_compare(self):
        list1 = [
            {'hostname': 'A', 'port': 1, 'region': 'ap-south-1'},
            {'hostname': 'A', 'port': 2, 'region': 'ap-south-1'},
            {'hostname': 'B', 'port': 1, 'region': 'me-central-1'},
        ]

        list2 = [
            {'host': 'A', 'port': 1, 'vendor': 'ACME'},
            {'host': 'B', 'port': 1, 'vendor': 'NotACME'},
            {'host': 'B', 'port': 2, 'vendor': 'NotACME'},
        ]

        result = compare_lists(
            list1,
            list2,
            lambda x, y: x['hostname'] == y['host'] and x['port'] == y['port']
        )

        # pprint(result)
        print(json.dumps(result))
        assert(
            'matched' in result and
            '+' in result and
            '-' in result
        )
        assert(
            len(result['matched']) == 2 and
            len(result['+']) == 1 and
            len(result['-']) == 1
        )

        result = lookup_lists(
            list1,
            list2,
            lambda x, y: x['hostname'] == y['host'] and x['port'] == y['port']
        )

        print(json.dumps(result))
        # TODO: Assert
