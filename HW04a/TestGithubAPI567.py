import unittest
import GithubAPI567
from GithubAPI567 import github, get_commits
from unittest.mock import Mock, patch


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

    def testValidUsername(self):
        username = "jolenec1002"
        mock_res = Mock()
        mock_res.content = '[{"name": "HomelessDataProject"}, {"name": "jolenec"}]'
        with patch('requests.get', return_value = mock_res):
            self.assertEqual(github(username), {'HomelessDataProject': 2, 'jolenec': 2})

    def testCommits(self):
        user = "jolenec1002"
        repo = "repo1"
        fake_response = Mock()
        fake_response.content = '[{"commit": {"message": "commit message 1"}}, {"commit": {"message": "commit message 2"}}]'
        with patch('requests.get', return_value=fake_response):
            self.assertEqual(get_commits(user, repo), 2)


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
    