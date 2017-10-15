# Unittest file for Sprint 1
import unittest
from BuhseFork import divBeforeMarr, deathBeforeMarr, deathBeforeBirth, deathBeforeDivorce, multipleBirths, tooManySiblings, correct_gender_for_role, male_last_names, tooOld, isUniqueID, isUniqueNameAndBirth


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
        individuals = {'1': {'birthday': ['23', 'FEB', '1970']},
                       '2': {'birthday': ['23', 'FEB', '1970']},
                       '3': {'birthday': ['23', 'FEB', '1970']},
                       '4': {'birthday': ['23', 'FEB', '1970']},
                       '5': {'birthday': ['23', 'FEB', '1970']},
                       '6': {'birthday': ['23', 'FEB', '1970']}}
        self.assertFalse(multipleBirths("NA", individuals))
        self.assertFalse(multipleBirths(['1'], individuals))
        self.assertFalse(multipleBirths(['1', '2'], individuals))
        self.assertFalse(multipleBirths(['1', '2', '3', '4', '5'], individuals))
        self.assertTrue(multipleBirths(['1', '2', '3', '4', '5', '6'], individuals))

    def testTooManySiblings(self):
        self.assertFalse(tooManySiblings([]))
        self.assertFalse(tooManySiblings(['a']))
        self.assertFalse(tooManySiblings(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']))
        self.assertTrue(tooManySiblings(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p']))
        self.assertTrue(tooManySiblings(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']))

    # ----------------------------------

    # Tests written by Jacob Ulasevich
    def testTooOld(self):
        self.assertFalse(tooOld(1))
        self.assertFalse(tooOld(100))
        self.assertFalse(tooOld(11))
        self.assertTrue(tooOld(150))
        self.assertTrue(tooOld(190))

    def testUniqueID(self):
        uniqueIDs = [1, 2, 3, 4, 5]
        uniqueFamIDs = [1, 2, 3, 4, 5]
        self.assertTrue(isUniqueID(100, "INDI"))
        self.assertFalse(isUniqueID(3, "INDI"))
        self.assertTrue(isUniqueID(100, "FAM"))
        self.assertFalse(isUniqueID(3, "FAM"))
        self.assertFalse(isUniqueID(1, "FAM"))

    def testUniqueNameAndBirthday(self):
        uniqueNameAndBirth = {'5APR1986': ['Dana/Ulasevich/'], '26AUG2085': ['Kyle/Pollock/'], '31JUL1962': ['Gary/Wood/']}
        self.assertTrue(isUniqueNameAndBirth('Jacob/Adam/', ['6', 'FEB', '1996']))
        self.assertTrue(isUniqueNameAndBirth('Alex/Wood/', ['20', 'FEB', '1990']))
        self.assertFalse(isUniqueNameAndBirth('Dana/Ulasevich/', ['5', 'APR', '1986']))
        self.assertFalse(isUniqueNameAndBirth('Gary/Wood/', ['31', 'JUL', '1962']))
        self.assertTrue(isUniqueNameAndBirth('James/Wood/', ['20', 'FEB', '1990']))

    # ----------------------------------

    # Tests written by Greyson Strouse
    def testDivorceBeforeDeath(self):
        self.assertFalse(deathBeforeDivorce(['16', 'MAY', '2000'], ['16', 'MAY', '2005']))
        self.assertTrue(deathBeforeDivorce(['16', 'MAY', '2008'], ['16', 'MAY', '2005']))
        self.assertTrue(deathBeforeDivorce(['16', 'MAR', '2000'], ['16', 'FEB', '2000']))
        self.assertTrue(deathBeforeDivorce(['17', 'MAY', '2000'], ['16', 'MAY', '2000']))
        self.assertFalse(deathBeforeDivorce(['16', 'MAY', '2000'], ['16', 'MAY', '2000']))

    def testDeathBeforeBirth(self):
        self.assertFalse(deathBeforeBirth(['16', 'MAY', '2000'], ['16', 'MAY', '2005']))
        self.assertTrue(deathBeforeBirth(['16', 'MAY', '2008'], ['16', 'MAY', '2005']))
        self.assertTrue(deathBeforeBirth(['16', 'MAR', '2000'], ['16', 'FEB', '2000']))
        self.assertTrue(deathBeforeBirth(['17', 'MAY', '2000'], ['16', 'MAY', '2000']))
        self.assertFalse(deathBeforeBirth(['16', 'MAY', '2000'], ['16', 'MAY', '2000']))

    def testMaleLastNames(self):
        "False if last names do not mactch, true if they do."
        self.assertFalse(male_last_names([14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29],
                                         {'marrDate': ['10', 'FEB', '1973'], 'divDate': 'NA', 'husband': 6, 'wife': 4,
                                          'children': [14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29],
                                          'endDate': [['18', 'MAR', '1986'], 'Husband']},-1))
        self.assertTrue(male_last_names([3, 10, 11, 12],{'marrDate': ['12', 'MAY', '1899'], 'divDate': 'NA',
                                                         'husband': 6, 'wife': 7, 'children': [3, 10, 11, 12],
                                                         'endDate': [['10', 'APR', '1975'], 'Wife']},-1))

    def testCorrectGenderForRole(self):
        "False if gender for role is incorrect."
        self.assertFalse(correct_gender_for_role(2,{'marrDate': ['15', 'MAY', '1982'], 'divDate': ['15', 'FEB', '1981'],
                                                    'husband': 2, 'wife': 3, 'children': [1, 4, 5], 'endDate':
                                                        [['19', 'MAR', '1975'], 'Husband']}))
        self.assertTrue(correct_gender_for_role(6,{'marrDate': ['10', 'FEB', '1973'], 'divDate': 'NA',
                                                   'husband': 6, 'wife': 4, 'children': [9], 'endDate':
                                                       [['18', 'MAR', '1986'], 'Husband']}))



if __name__ == '__main__':
    unittest.main()
