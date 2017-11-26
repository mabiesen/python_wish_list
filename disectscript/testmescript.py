## should allow for pulling all classnames from scripts
## option to pull all methods

## should allow for pulling all function initiations

## should allow for pulling all global variables
## option to count number of global variables

## move through all files in directory and perform one or more of the above operations

## SHOULD BE A CLI BASED TOOL WITH PRINT OUTPUT.


import click
import re

functionList = []
globalVarList = []


def get_file_lines(file):
  fh = open(filename, "r")
  return fh.readlines()

def get_defs(fileLines):
    for f in fileLines:
        if "def " in f:
            functionList.append(f)

def get_global_vars(fileLines):
    '''use regex to insure no tabs or spaces precede <word>='''
    for f in fileLines:
        if re.match(r"^\w{1,30}\b\s=", f) or re.match(r"^\w{1,30}\b=", f):
            globalVarList.append(f)

@click.command()
@click.option('--file', help='python file to dissect')
@click.option('--which', default="all", help='choose the data you would like to collect. all for all, g for globals, f for function')
def summary(file,which,write):
   '''Simple program to group python defs/classnames/globalvars'''
   fileLines = get_file_lines(file)
   get_defs(fileLines)
   get_global_vars(fileLines)

   if which == "all":
       print("functions:")
       print(functionList)
       print("")
       print("global variables:")
       print(globalVarList)

if __name__ == '__main__':
   summary()
