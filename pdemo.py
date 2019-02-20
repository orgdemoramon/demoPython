import sys, getopt

def help():
    print("Script to modify a pom file based on github organization and branch name")
    print("Usage: python3 pdemo.py path_local_repo")
    print("Usage: Python3 pdemo.py /my/awesome/repo")
    print("pom file needs to be in the root of your repo, .git folder also needs to be present")

def stringFunc(pathGit):
    from git import Repo
    from urllib.parse import urlparse
    repo = Repo(pathGit)
    branch = str(repo.active_branch)
    org = urlparse(repo.remotes.origin.url).path.split('/')[1]
    return "ci_"+org+"_"+branch+"-SNAPSHOT"
    
def pomFunc(pom_File, pathGit):
    import xml.etree.ElementTree as ET
    nameSpace = "http://maven.apache.org/POM/4.0.0"
    ET.register_namespace('', nameSpace)
    tree = ET.ElementTree()
    tree.parse(pom_File)
    version = tree.getroot().find("{%s}version" %nameSpace )
    version.text=stringFunc(pathGit)
    tree.write(pom_File)

def main(argv):
    try:
        opts, args = getopt.getopt(argv,"h:p:", ["help=","path="])
    except getopt.GetoptError as err:
        print("Something went wrong")
        print(err)
        help()
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            help()
            sys.exit()
        elif opt in ('-p','--path'):
            path = arg
            gitPath = path + "/.git"
            pomFile = path + "/pom.xml"
            pomFunc(pomFile, gitPath)
            
if len(sys.argv) <= 1:
    print("Argument required")
    help()
    exit(1)
    
if __name__ == "__main__":
   main(sys.argv[1:])
