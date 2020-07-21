# L1ghtSab3r

L1ghtSab3r is a framework aimed to exploit Continuous Integration systems.

## Structure
During our research, we started off by testing our tool on github but we realized that doing so violate the CFAA. so we decided to 
setup a gitlab instance and test it there. 
We broke up the modules into the types of CI servers like travis, circle-ci and so on. This method helped us know exactly what server we plan to attack. Inside of each CI server folder, we broke it down to the exact type of attack like enumeration which would contain the malicious ci file. Here's a visual of the folder structure.

```
.
├── gitlab
│   ├── enum
│   │   ├── .gitlab-ci.yml
│   │   └── gitlabEnum.py
│   ├── nmap
│   │   └── gitlab-nmap.py
│   └── reverse_shell
│       └── gitlab-shell.py
└── travis
    ├── enum
    │   ├── .travis.yml
    │   └── enum.py
    ├── nmap
    │   ├── .travis.yml
    │   └── nmap.py
    └── reverse_shell
        ├── .travis.yml
        └── shell.py
```

## Modules

We want others to implement their own modules, so we have a module template where you can specify the platorm you are attacking(`github` or `gitlab`) and info about your module. 
Can be found in the modules folder.


## Config
Since github and gitlab are different platorm, you would need to get individual tokens from them. 

```
GITHUB_TOKEN = "" # Create one at https://github.com/settings/tokens
GITLAB_TOKEN = "" # Create one at https://gitlab.com/profile/personal_access_tokens
CUSTOM_GITLAB = "http://gitlab.example.com" # replace with gitlab url if not custom
GITLAB_USERNAME = ""
```

## Usage

```
$ chmod +x main.py
$ ./main.py
```

## Contributors
 - @PabloPotat0
 - @Th3QuantumJ3d1