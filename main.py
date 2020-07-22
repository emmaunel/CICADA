#!/usr/bin/python3  

#   _____ _____ _____          _____          
#  / ____|_   _/ ____|   /\   |  __ \   /\    
# | |      | || |       /  \  | |  | | /  \   
# | |      | || |      / /\ \ | |  | |/ /\ \  
# | |____ _| || |____ / ____ \| |__| / ____ \ 
#  \_____|_____\_____/_/    \_\_____/_/    \_\
                                             

from cmd import Cmd
import os
from common import modules
import gitlab


try:
    import gnureadline
    import sys
    sys.modules['readline'] = gnureadline
except ImportError:
    pass

banner = """
   _____ _____ _____          _____          
  / ____|_   _/ ____|   /\   |  __ \   /\    
 | |      | || |       /  \  | |  | | /  \   
 | |      | || |      / /\ \ | |  | |/ /\ \  
 | |____ _| || |____ / ____ \| |__| / ____ \ 
  \_____|_____\_____/_/    \_\_____/_/    \_\
"""

# targets = ["github.com/test"]
# TODO
# 1) fork all targets
# 2) clone forked targets
# 3) 
# 4) load poison yml file to forked targets
# 5) push commit changes, and submit pull request
# 6) Listen for incoming messages.

#TODO: Ask if they are using a custom gitlab instance

GITHUB_TOKEN = ""
GITLAB_TOKEN = "w_z7Ae4xvggSU3wLjizB"
CUSTOM_GITLAB = "http://gitlab.example.com"
GITLAB_USERNAME = "test"

class color:
    HEADER = '\033[95m'
    IMPORTANT = '\33[35m'
    NOTICE = '\033[33m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    RED = '\033[91m'
    END = '\033[0m'
    UNDERLINE = '\033[4m'
    LOGGING = '\33[34m'


class Terminal(Cmd):
    prompt = "(CICADA) >>> "
    targets = ["root/ci-test"]
    listerners = []
    loadedModule = None
    SETOPTIONS = ['target', 'module']

    def __init__(self):
        Cmd.__init__(self)
        self.installPath = os.getcwd()

    def do_exit(self, args):
        "Exit the framework"
        print("Byee")
        os._exit(0)

    def do_clear(self, args):
        os.system("clear")

    def do_listerners(self, args):
        "Your Listerners"
        print("Here are your listerners...")
        if len(self.listerners) == 0:
            print("No listerners")
        else:
            for listerner in self.listerners:
                print(listerner)

    def do_modules(self, args):
        "Availble modules"
        print("Listing availble modules...")
        self.printModules()

    def do_targets(self, args):
        "Lists of your targets"
        if len(self.targets) == 0:
            print("No targets")
        else:
            for target in self.targets:
                print(target)

    def do_set(self, args):
        """Add a target/module
        set target [target_link]
        set target <namespace>/<projectname>
        set module travis/enum"""

        arg = args.split()
        if arg[0] == "target":
            self.targets.append(arg[1])
        elif arg[0] == "module":
            ## check if module exist
            if self.checkModules(arg[1]):
                self.loadedModule = arg[1]
                print(self.loadedModule)
                #Change the prompt
                genModule = modules.ModuleMenu(self.loadedModule, self.installPath)
                genModule.cmdloop()
            else:
                print("Module doesn't exit")

    # TODO: DONT;t work
    def complete_set(self, text, line, begidx, endidx):
        if not text:
            completions = self.SETOPTIONS[:]

        return completions

    def do_unset(self, args):
        """Remove target
        unset target [target_link]"""
        arg = args.split()
        if arg[0] == "target":
            self.targets.remove(arg[1])

    def do_interact(self, args):
        "Interact with targets"

    # TODO: filter out some useless directory
    def printModules(self):
        file  = os.walk("./modules")
        for dir, dirs, files in file:
            print(dir)

    def checkModules(self, dir):
        path = "./modules"
        if os.path.isdir(path + "/" + dir):
            return True
        else:
            return False
    

def welcome():
    print(banner)
    # print("Welcome!!! May the force be with you")
    print("Created by PabloPotat0 & Th3QuantumJ3d1")
    print("CI Exploitation framework")


def main():
    welcome()
    terminal = Terminal()
    terminal.cmdloop()
                                          
if __name__ == "__main__":
    main()                                                                 