#!/usr/bin/python3  

#  _     __  _____ _    _ _______ _____         ____ ____  _____  
# | |   /_ |/ ____| |  | |__   __/ ____|  /\   |  _ \___ \|  __ \ 
# | |    | | |  __| |__| |  | | | (___   /  \  | |_) |__) | |__) |
# | |    | | | |_ |  __  |  | |  \___ \ / /\ \ |  _ <|__ <|  _  / 
# | |____| | |__| | |  | |  | |  ____) / ____ \| |_) |__) | | \ \ 
# |______|_|\_____|_|  |_|  |_| |_____/_/    \_\____/____/|_|  \_\
#

from cmd import Cmd
import os
from common import modules


try:
    import gnureadline
    import sys
    sys.modules['readline'] = gnureadline
except ImportError:
    pass

banner = """
   _     __  _____ _    _ _______ _____         ____ ____  _____  
  | |   /_ |/ ____| |  | |__   __/ ____|  /\   |  _ \___ \|  __ \ 
  | |    | | |  __| |__| |  | | | (___   /  \  | |_) |__) | |__) |
  | |    | | | |_ |  __  |  | |  \___ \ / /\ \ |  _ <|__ <|  _  / 
  | |____| | |__| | |  | |  | |  ____) / ____ \| |_) |__) | | \ \ 
  |______|_|\_____|_|  |_|  |_| |_____/_/    \_\____/____/|_|  \_\
"""

# targets = ["github.com/test"]
# TODO
# 1) fork all targets
# 2) clone forked targets
# 3) 
# 4) load poison yml file to forked targets
# 5) push commit changes, and submit pull request
# 6) Listen for incoming messages.



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
    prompt = "(L1GHTSAB3R) >>> "
    targets = []
    listerners = []
    loadedModule = None
    SETOPTIONS = ['target', 'module']

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
        set target github.com/<username>/<repo>
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
                newPrompt = self.prompt[:-5] + " [" + color.RED + arg[1] + color.END + "]  >>> " # <----- Terrible way
                genModule = modules.Module(newPrompt, self.loadedModule)
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
    print("Welcome!!! May the force be with you")
    print("Created by PabloPotat0 & Th3QuantumJ3d1")
    print("CI Exploitation framework")


def main():
    welcome()
    terminal = Terminal()
    terminal.cmdloop()
                                          
if __name__ == "__main__":
    main()                                                                 