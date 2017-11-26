## should allow for pulling all classnames from scripts
## option to pull all methods

## should allow for pulling all function initiations

## should allow for pulling all global variables
## option to count number of global variables

## move through all files in directory and perform one or more of the above operations

## SHOULD BE A CLI BASED TOOL WITH PRINT OUTPUT.


import click
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

@click.command()
@click.option('--file', help='python file to dissect')
def summary(file):
   fileLines = get_file_lines(file)
   get_global_defs(fileLines)
   get_global_vars(fileLines)
   get_global_imports(fileLines)

   filename = os.path.basename(file)

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

if __name__ == '__main__':
   summary()
