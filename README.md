# demoPython

Python script to modify pom.xml based on github organization and branch  

## Prerequisites

In order to install all the required dependencies please follow the next instructions:
* Python3 needs to be installed in your local system

```
git clone https://github.com/orgdemoramon/demoPython.git
virtualenv demoPython/
cd demoPython && source bin/activate
pip3 install -r requirements.txt
```
## Executing python script
```
python3 pdemo.py -p /path/to/your/repo
```

Both .git directory and pom.xml need to be located in this repo

## Help
```
python3 pdemo.py -h
```
Show help
