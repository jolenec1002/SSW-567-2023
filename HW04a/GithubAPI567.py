import requests
import json
import re
from mybrand import my_brand
my_brand("SSW 567 HW 04a-Develop with the Perspective of the Tester in Mind")

dict = {}
def github(username):

    if not(is_valid(username)):
        return "Invalid Input"
    
    api_url = "https://api.github.com/users/" + username + "/repos"
    req = requests.get(api_url)
    repo = json.loads(req.content)
    rVal = {}
      
    for repo_object in repo:
        commitNom = get_commits(username,repo_object['name'])
        rVal[repo_object['name']] = commitNom

    return rVal

def get_commits(user,repo):
    commit = "https://api.github.com/repos/" + user + "/" + repo + "/commits"
    getReq = requests.get(commit)
    commitContent = json.loads(getReq.content)
    return len(commitContent)

def is_valid(username):
    symbols = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
    double_hyphen = re.compile('--')
    # Checking for valid inputs
    # Username cannot be empty, cannot be multiple words, and cannot be more than 39 characters
    if (username == "") or (' ' in username) or len(username) > 39:
        return False
    # As per Github guidelines, username can't have any symbols except a hyphen
    # The hyphen can't be at the beginning or at the end, and there cannot be a double hyphen anywhere
    elif (symbols.search(username) != None) or (username.endswith("-")) or (double_hyphen.search(username) != None) or (username.startswith("-")):
        return False
    else:
        return True


print(github("jolenec1002"))
my_brand("SSW 567 HW 04a-Develop with the Perspective of the Tester in Mind")





