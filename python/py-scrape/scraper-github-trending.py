import requests
from bs4 import BeautifulSoup


page = requests.get('https://github.com/trending')

# Create a BeautifulSoup object
soup = BeautifulSoup(page.text, 'html.parser')

# get the repo list
repo = soup.find(class_="Box-row")
#repo = soup.find(class_="h3 lh-condensed")

print(len(repo))
print(repo)

# find all instances of that class (should return 25 as shown in the github main page)
repo_list = repo.find_all(class_="text-normal")

print(len(repo_list))
print(repo_list)
