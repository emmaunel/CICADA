from cmd import Cmd

class Module(Cmd):
    prompt = ""
    ## Use this to get different info??
    loadedModule = None

    def __init__(self, args, mod):
        Cmd.__init__(self)
        self.prompt = args
        self.loadedModule = mod

    def do_back(self, args):
        "Exit the module"
        return True

    def do_exit(self, args):
        "Exit the module"
        return True

    def do_info(self, args):
        "Give info about module"
        print("info")


    def do_exploit(self, args):
        "Run the exploit"
        print("Attackkkk")