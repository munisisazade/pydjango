import os
import sys
import subprocess
from pydjango.main.detect import os_type


class Command(object):
    """
        Application base logic class
    """

    def __init__(self, folder_name):
        """
            Initialize folder name
        """
        self.folder_name = folder_name
        self.path = "%s/" % folder_name if os_type != "Windows" else "%s\\" % folder_name

    def run(self):
        """
            This method start all methods
        """
        self.create_folder()
        if os_type == "Linux":
            print("Linux")
        elif os_type == "Windows":
            sys.stdout.write("First install VirtualEnv for windows...\n")
            self.run_win_cmd("pip install virtualenv virtualenvwrapper-win")
            sys.stdout.write("Creating virtualenv for python3...\n")
            self.run_win_cmd('mkvirtualenv "%cd%\\' + '%s%s"' % (self.path, "venv"))
            sys.stdout.write("Activate virtualenv and install django...\n")
            self.run_win_cmd("%s%s\\Scripts\\activate.bat && pip install django" % (self.path, "venv"))
            sys.stdout.write("Create new django app \n")
            djang_app_name = input("Django app name: ")
            self.run_win_cmd("%s%s\\Scripts\\activate.bat && django-admin startproject %s %s" % (self.path, "venv", djang_app_name, self.path))
            app_name = input("Application name : ")
            self.run_win_cmd("%s%s\\Scripts\\activate.bat && python manage.py startapp %s" % (
            self.path, "venv", app_name))
            print("Yess !!!")
            print("Windows")
        elif os_type == "Darwin":
            print("Mac")
        else:
            sys.stdout.write("Error: cannot detect Operation System %s\n" % os_type)
            sys.exit(1)

    def run_win_cmd(self, commands):
        result = []
        process = subprocess.Popen(commands,
                                   shell=True,
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE)
        for line in process.stdout:
            result.append(line)
        errcode = process.returncode
        for line in result:
            sys.stdout.write(line.decode("utf-8"))
        if errcode is not None:
            raise Exception('cmd %s failed, see above for details', commands)

    def create_folder(self):
        os.makedirs(self.folder_name)
