#! /usr/local/bin/python3

import xml.etree.ElementTree as ET
from git import Repo
from urllib.parse import urlparse


ns = "http://maven.apache.org/POM/4.0.0"
ET.register_namespace('', ns)
tree = ET.ElementTree()
tree.parse('pom.xml')
p = tree.getroot().find("{%s}version" %ns )

repo = Repo('.')

branch = repo.active_branch
print(branch)
url = repo.remotes.origin.url
BRANCH=str(branch)

org = urlparse(url)
org=org.path.split('/')[1]
print(org)
final_string="ci_"+org+"_"+BRANCH+"-SNAPSHOT"
print(final_string)
p.text=final_string
tree.write('pom.xml')
