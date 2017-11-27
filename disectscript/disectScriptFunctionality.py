import re
import os



class DisectScript:

    functionList = []
    globalVarList = []
    importList = []

    def get_file_lines(self,filename):
      fh = open(filename, "r")
      return fh.readlines()

    def get_global_imports(self,fileLines):
        for f in fileLines:
            if re.match(r"^import\s", f):
                self.importList.append(f.rstrip())

    def get_global_defs(self,fileLines):
        for f in fileLines:
            if re.match(r"^def\s", f):
                self.functionList.append(f.rstrip())

    def get_global_vars(self,fileLines):
        '''use regex to insure no tabs or spaces precede <word>='''
        for f in fileLines:
            if re.match(r"^\w{1,30}\b\s=", f) or re.match(r"^\w{1,30}\b=", f):
                self.globalVarList.append(f.rstrip())

    def print_all(self,filename):
       print("")
       print("-------FILE SUMMARY FOR " + filename + "-------")
       print("")
       print("GLOBAL IMPORTS:")
       for i in self.importList:
           print(i)
       print("")
       print("GLOBAL FUNCTIONS:")
       for i in self.functionList:
           print(i)
       print("")
       print("GLOBAL VARIABLES:")
       for i in self.globalVarList:
           print(i)

def main_func(file):
    ds = DisectScript()
    fileLines = ds.get_file_lines(file)
    ds.get_global_defs(fileLines)
    ds.get_global_vars(fileLines)
    ds.get_global_imports(fileLines)

    filename = os.path.basename(file)

    ds.print_all(filename)
