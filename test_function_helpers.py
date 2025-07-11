import unittest, sys
from pappardelle import CacheOrLambda

sys.path.append('pappardelle')  # Include the subdir in the PythonPath

counters = {}

class TestStringHelpers(unittest.TestCase):
    def test_cache_or_lambda(self):
        counters['col1'] = 0
        col1 = CacheOrLambda(
            cache_fetch
        )
        col1.fetch("a")
        print(counters['col1'])
        col1.fetch("a")
        print(counters['col1'])


def cache_fetch(a_key):
    counters['col1'] += 1
    return counters['col1']
