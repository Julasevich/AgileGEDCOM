# Unittest file for Sprint 1
import unittest
from Project02 import divBeforeMarr, deathBeforeMarr


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

    # Tests written by ...


if __name__ == '__main__':
    unittest.main()
