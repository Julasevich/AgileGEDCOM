# Unittest file for Sprint 1
import unittest
from BuhseFork import divBeforeMarr, deathBeforeMarr, deathBeforeBirth, deathBeforeDivorce, multipleBirths, tooManySiblings


class TestGEDCOM(unittest.TestCase):


    # Tests written by Christopher Frost
    def testMarrBeforeDeath(self):
        self.assertFalse(deathBeforeMarr(['23', 'FEB', '1970'], ['23', 'FEB', '1996']))
        self.assertTrue(deathBeforeMarr(['23', 'FEB', '1996'], ['23', 'FEB', '1970']))
        self.assertTrue(deathBeforeMarr(['23', 'MAR', '1970'], ['23', 'FEB', '1970']))
        self.assertTrue(deathBeforeMarr(['24', 'FEB', '1970'], ['23', 'FEB', '1970']))
        self.assertFalse(deathBeforeMarr(['23', 'FEB', '1970'], ['23', 'FEB', '1970']))

    def testMarrBeforeDiv(self):
        self.assertFalse(divBeforeMarr(['23', 'FEB', '1970'], ['23', 'FEB', '1996']))
        self.assertTrue(divBeforeMarr(['23', 'FEB', '1996'], ['23', 'FEB', '1970']))
        self.assertTrue(divBeforeMarr(['23', 'MAR', '1970'], ['23', 'FEB', '1970']))
        self.assertTrue(divBeforeMarr(['24', 'FEB', '1970'], ['23', 'FEB', '1970']))
        self.assertFalse(divBeforeMarr(['23', 'FEB', '1970'], ['23', 'FEB', '1970']))

    def testMultipleBirths(self):
        self.assertFalse(multipleBirths())
        self.assertFalse(multipleBirths())
        self.assertFalse(multipleBirths())
        self.assertFalse(multipleBirths())
        self.assertFalse(multipleBirths())

    def testTooManySiblings(self):
        self.assertFalse(tooManySiblings([]))
        self.assertFalse(tooManySiblings(['a']))
        self.assertFalse(tooManySiblings(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']))
        self.assertTrue(tooManySiblings(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p']))
        self.assertTrue(tooManySiblings(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']))

    # ----------------------------------

    # Tests written by Greyson Strouse
    def testDivorceBeforeDeath(self):
        self.assertTrue(deathBeforeDivorce(['16', 'MAY', '2000'], ['16', 'MAY', '2005']))
        self.assertFalse(deathBeforeDivorce(['16', 'MAY', '2008'], ['16', 'MAY', '2005']))
        self.assertFalse(deathBeforeDivorce(['16', 'MAR', '2000'], ['16', 'FEB', '2000']))
        self.assertFalse(deathBeforeDivorce(['17', 'MAY', '2000'], ['16', 'MAY', '2000']))
        self.assertTrue(deathBeforeDivorce(['16', 'MAY', '2000'], ['16', 'MAY', '2000']))

    def testBirthBeforeDeath(self):
        self.assertTrue(deathBeforeBirth(['16', 'MAY', '2000'], ['16', 'MAY', '2005']))
        self.assertFalse(deathBeforeBirth(['16', 'MAY', '2008'], ['16', 'MAY', '2005']))
        self.assertFalse(deathBeforeBirth(['16', 'MAR', '2000'], ['16', 'FEB', '2000']))
        self.assertFalse(deathBeforeBirth(['17', 'MAY', '2000'], ['16', 'MAY', '2000']))
        self.assertTrue(deathBeforeBirth(['16', 'MAY', '2000'], ['16', 'MAY', '2000']))


if __name__ == '__main__':
    unittest.main()
