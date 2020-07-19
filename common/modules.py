from cmd import Cmd
import main

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

    def do_targets(self, args):
        "Lists of your targets"
        if len(main.Terminal.targets) == 0:
            print("No targets")
        else:
            for target in main.Terminal.targets:
                print(target)

    # def do_set(self, args):
    #     arg = args.split()
    #     if arg[0] == "target":
    #         main.Terminal.targets.append(arg[1])
    #     else:
    #         print("Command unknown")

    def do_exploit(self, args):
        "Run the exploit"
        print("Attackkkk")