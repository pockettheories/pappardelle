import unittest
from test_date_helpers import TestDateHelpers
from test_list_helpers import TestListHelpers
from test_dict_helpers import TestDictHelpers
from test_string_helpers import TestStringHelpers


def run_some_tests():
    test_classes_to_run = [TestDateHelpers, TestListHelpers, TestDictHelpers, TestStringHelpers]
    loader = unittest.TestLoader()

    suites_list = []

    for test_class in test_classes_to_run:
        suite = loader.loadTestsFromTestCase(test_class)
        suites_list.append(suite)

    big_suite = unittest.TestSuite(suites_list)

    runner = unittest.TextTestRunner()
    results = runner.run(big_suite)


if __name__ == '__main__':
    run_some_tests()
