import re
import os

functionList = []
globalVarList = []
importList = []


def get_file_lines(filename):
  fh = open(filename, "r")
  return fh.readlines()

def get_global_imports(fileLines):
    for f in fileLines:
        if re.match(r"^import\s", f):
            importList.append(f.rstrip())

def get_global_defs(fileLines):
    for f in fileLines:
        if re.match(r"^def\s", f):
            functionList.append(f.rstrip())

def get_global_vars(fileLines):
    '''use regex to insure no tabs or spaces precede <word>='''
    for f in fileLines:
        if re.match(r"^\w{1,30}\b\s=", f) or re.match(r"^\w{1,30}\b=", f):
            globalVarList.append(f.rstrip())

def print_all(filename):
   print("")
   print("-------FILE SUMMARY FOR " + filename + "-------")
   print("")
   print("GLOBAL IMPORTS:")
   for i in importList:
       print(i)
   print("")
   print("GLOBAL FUNCTIONS:")
   for i in functionList:
       print(i)
   print("")
   print("GLOBAL VARIABLES:")
   for i in globalVarList:
       print(i)
