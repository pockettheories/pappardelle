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

        ##
        ## Compare Lists
        ##

        result = compare_lists(
            list1,
            list2,
            lambda x, y: x['hostname'] == y['host'] and x['port'] == y['port']
        )

        # pprint(result)
        print(json.dumps(result))

        # We should have the +, -, = irrespective of the results
        assert(
            '=' in result and
            '+' in result and
            '-' in result
        )

        # Ensure the lengths of the lists match
        assert(
            len(result['=']) == 2 and
            len(result['+']) == 1 and
            len(result['-']) == 1
        )

        # Check the actual contents of the list to ensure we don't have it reversed
        # It's OK to index the list in the test because we have only 1 element for these
        assert(
            result['+'][0]['hostname'] == 'A' and
            result['+'][0]['port'] == 2 and
            result['+'][0]['region'] == 'ap-south-1'
        )
        assert(
            result['-'][0]['host'] == 'B' and
            result['-'][0]['port'] == 2 and
            result['-'][0]['vendor'] == 'NotACME'
        )

        try:
            result['='].index(list1[0])
            result['='].index(list1[2])
        except ValueError:
            raise Exception("match list does not contain the expected elements")

        ##
        ## Lookup Lists
        ##

        result = lookup_lists(
            list1,
            list2,
            lambda x, y: x['hostname'] == y['host'] and x['port'] == y['port']
        )

        print(json.dumps(result))
        # TODO: Assert
