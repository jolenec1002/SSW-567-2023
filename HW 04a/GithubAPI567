import requests
import json
from github import Github
import re
from mybrand import my_brand
my_brand("SSW 567 HW 04a-Develop with the Perspective of the Tester in Mind")

dict = {}
def github(username):

    if not(is_valid(username)):
        return "Invalid Input"
    
    g = Github()
    user = g.get_user(username)
    repo_list = []
    global dict

    # Putting the Repository names in a list
    for repo in user.get_repos():
        repo_list.append(repo.full_name)

    to_remove = username + "/"
    # Removing the username from the Repository names
    for i in range(len(repo_list)):
        repo_list[i]=repo_list[i].replace(to_remove,"")
        repo_name = repo_list[i]

        # Setting up the API url for commits
        api_url = f"https://api.github.com/repos/" + username + "/" + repo_name + "/commits"
        com = requests.get(api_url)
        commits = json.loads(com.content)
        commits_number = len(commits) 
        dict[repo_name] = commits_number

    return dict

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


#print(github("jolenec1002"))
my_brand("SSW 567 HW 04a-Develop with the Perspective of the Tester in Mind")







