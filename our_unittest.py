# Unittest file for Sprint 1
import unittest
from Project02 import marrBeforeDiv, marrBeforeDeath


class TestGEDCOM(unittest.TestCase):

    # Tests written by Christopher Frost
    def testMarrBeforeDeath(self):
        self.assertTrue(marrBeforeDeath(['23', 'FEB', '1970'], ['23', 'FEB', '1996']))
        self.assertFalse(marrBeforeDeath(['23', 'FEB', '1996'], ['23', 'FEB', '1970']))
        self.assertFalse(marrBeforeDeath(['23', 'MAR', '1970'], ['23', 'FEB', '1970']))
        self.assertFalse(marrBeforeDeath(['24', 'FEB', '1970'], ['23', 'FEB', '1970']))
        self.assertTrue(marrBeforeDeath(['23', 'FEB', '1970'], ['23', 'FEB', '1970']))

    def testMarrBeforeDiv(self):
        self.assertTrue(marrBeforeDiv(['23', 'FEB', '1970'], ['23', 'FEB', '1996']))
        self.assertFalse(marrBeforeDiv(['23', 'FEB', '1996'], ['23', 'FEB', '1970']))
        self.assertFalse(marrBeforeDiv(['23', 'MAR', '1970'], ['23', 'FEB', '1970']))
        self.assertFalse(marrBeforeDiv(['24', 'FEB', '1970'], ['23', 'FEB', '1970']))
        self.assertTrue(marrBeforeDiv(['23', 'FEB', '1970'], ['23', 'FEB', '1970']))
    # ----------------------------------

    # Tests written by ...

if __name__ == '__main__':
    unittest.main()
