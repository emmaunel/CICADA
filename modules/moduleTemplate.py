class Module:
    def __init__(self):
        # Where is the CI server hosted, github or gitlab
        self.type = ""

    def info(self):
        "Give info about module"
        print("What does this module do")