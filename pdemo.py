#! /usr/local/bin/python3

import xml.etree.ElementTree as ET
from github import Github
from git import Repo

ns = "http://maven.apache.org/POM/4.0.0"
ET.register_namespace('', ns)
tree = ET.ElementTree()
tree.parse('pom.xml')
p = tree.getroot().find("{%s}version" %ns )

print(p.text)

g = Github("mental1234", "******")
for repo in g.get_user().get_repos():
    print(repo.name)
    


repo = Repo('.')
repoName = repo.remote
branch = repo.active_branch

print(branch)
print(repoName)
