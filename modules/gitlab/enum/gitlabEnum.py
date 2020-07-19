from cmd import Cmd

class Module(Cmd):
    prompt = ""

    def __init__(self, args):
        Cmd.__init__(self)
        self.prompt = args

    def do_back(self, args):
        "Exit the module"
        return True

    def do_info(self, args):
        "Give info about module"
        print("info")


    def do_exploit(self, args):
        "Run the exploit"
        print("Attackkkk")