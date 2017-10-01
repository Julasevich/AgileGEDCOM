# Unittest file for Sprint 1
import unittest
from Project02 import divBeforeMarr, deathBeforeMarr, birth_before_death, div_before_death


class TestGEDCOM(unittest.TestCase):


    # Tests written by Christopher Frost
    def testMarrBeforeDeath(self):
        self.assertTrue(deathBeforeMarr(['23', 'FEB', '1970'], ['23', 'FEB', '1996'], ['23', 'FEB', '1971']))
        self.assertFalse(deathBeforeMarr(['23', 'FEB', '1996'], ['23', 'FEB', '1970', ['19', 'OCT', '1996']]))
        self.assertFalse(deathBeforeMarr(['23', 'MAR', '1970'], ['23', 'FEB', '1970', ['28', 'MAR', '1996']]))
        self.assertFalse(deathBeforeMarr(['24', 'FEB', '1970'], ['23', 'FEB', '1970', ['01', 'JUL', '1996']]))
        self.assertTrue(deathBeforeMarr(['23', 'FEB', '1970'], ['23', 'FEB', '1970'], ['23', 'FEB', '1970']))

    def testMarrBeforeDiv(self):
        self.assertTrue(divBeforeMarr(['23', 'FEB', '1970'], ['23', 'FEB', '1996']))
        self.assertFalse(divBeforeMarr(['23', 'FEB', '1996'], ['23', 'FEB', '1970']))
        self.assertFalse(divBeforeMarr(['23', 'MAR', '1970'], ['23', 'FEB', '1970']))
        self.assertFalse(divBeforeMarr(['24', 'FEB', '1970'], ['23', 'FEB', '1970']))
        self.assertTrue(divBeforeMarr(['23', 'FEB', '1970'], ['23', 'FEB', '1970']))
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
