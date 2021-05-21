import os
import tempfile
import random

class File:
    def __init__(self, path_to_file):
        self.path_to_file = path_to_file
        if  not os.path.exists(path_to_file):
            with open(self.path_to_file, "w") as f:
                f.write("")
    def read(self):
        try:
            with open(self.path_to_file, "r") as f:
                return f.read()
        except Exception: 
            return "Something go wrong with read()"
    def readlines(self):
        try:
            with open(self.path_to_file, "r") as f:
                return f.readlines()
        except Exception: 
            return "Something go wrong with readlines()"
    def __str__(self):
        return str(self.path_to_file)
    def write(self, text):
        with open(self.path_to_file, "w") as f:
            f.write(text)
    def __add__(self, obj):
        try:
            plus = str(self.read()) + str(obj.read())
            res_file = File(os.path.join(tempfile.gettempdir(), "new_file"+str(random.randint(1,999999))))
            res_file.write(plus)
            return res_file
        except Exception:
            return "Oooooops..."
    def __getitem__(self, index):
        return self.readlines()[index]

