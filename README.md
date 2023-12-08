# OSINT Search

OSINT scripts to mine and retrieve Yara and Sigma rules from Github repositories using Github search API.

## Installation

```
 git clone https://github.com/aitor-alvarez/OSINT-Search
 
 pip install -r requirements.txt
 
 Add GITHUB_API key in creds.py file
 
 ```
 
 After installation, the directory downloads/ will be created where the rules will be stored.

## Commands


For searching Sigma or Yara rules (without any optimization in the search) just use the -f argument followed by either string "yara" or "sigma" as shown below:

```
python main.py -f "sigma"
python main.py -f "yara"

```
 If a specific string needs to be in the content of the file, the argument -c will need to be passed:

```
python main.py -f "sigma" -c ".exe"
```

Similarly, any file  that contains a particular string can be retrieved in the following way:

```
python main.py -f "any" -c "function search_api()"
```
