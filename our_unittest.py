# Unittest file for Sprint 1
import unittest
from Project02 import marrBeforeDiv, marrBeforeDeath, birth_before_death, div_before_death


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

    # Tests written by Greyson Strouse
    def testDivorceBeforeDeath(self):
        self.assertTrue(div_before_death(['16', 'MAY', '2000'], ['16', 'MAY', '2005']))
        self.assertFalse(div_before_death(['16', 'MAY', '2008'], ['16', 'MAY', '2005']))
        self.assertFalse(div_before_death(['16', 'MAR', '2000'], ['16', 'FEB', '2000']))
        self.assertFalse(div_before_death(['17', 'MAY', '2000'], ['16', 'MAY', '2000']))
        self.assertTrue(div_before_death(['16', 'MAY', '2000'], ['16', 'MAY', '2000']))

    def testBirthBeforeDeath(self):
        self.assertTrue(birth_before_death(['16', 'MAY', '2000'], ['16', 'MAY', '2005']))
        self.assertFalse(birth_before_death(['16', 'MAY', '2008'], ['16', 'MAY', '2005']))
        self.assertFalse(birth_before_death(['16', 'MAR', '2000'], ['16', 'FEB', '2000']))
        self.assertFalse(birth_before_death(['17', 'MAY', '2000'], ['16', 'MAY', '2000']))
        self.assertTrue(birth_before_death(['16', 'MAY', '2000'], ['16', 'MAY', '2000']))

if __name__ == '__main__':
    unittest.main()
