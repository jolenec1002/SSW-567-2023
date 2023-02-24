import unittest
import GithubAPI567
from GithubAPI567 import github

from mybrand import my_brand
my_brand("SSW 567 HW 04a-Develop with the Perspective of the Tester in Mind")

class TestGithub(unittest.TestCase):

    def testInvalidInputs(self):
        self.assertEqual(github("-jolene"),'Invalid Input')
        self.assertEqual(github("jolene-"),'Invalid Input')
        self.assertEqual(github("two words"),'Invalid Input')
        self.assertEqual(github("&jjdj"),'Invalid Input')
        self.assertEqual(github("ajfdshsadfafhkhkakhadfkhdafkhfdkhfdkhdfhkfdkhfdahkfa"),'Invalid Input')
        self.assertEqual(github(""),'Invalid Input')
        self.assertEqual(github("hello--worlds"),'Invalid Input')

    def testValidUser(self):
        self.assertEqual(github("jolenec1002"),{'HomelessDataProject': 1, 'jolenec1002': 2})

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
    