## should allow for pulling all classnames from scripts
## option to pull all methods

## should allow for pulling all function initiations

## should allow for pulling all global variables
## option to count number of global variables

## move through all files in directory and perform one or more of the above operations

## SHOULD BE A CLI BASED TOOL WITH PRINT OUTPUT.


import click
from disectScriptFunctionality import *

@click.command()
@click.option('--file', help='python file to dissect')
def summary(file):
   fileLines = get_file_lines(file)
   get_global_defs(fileLines)
   get_global_vars(fileLines)
   get_global_imports(fileLines)

   filename = os.path.basename(file)

   print_all(filename)

if __name__ == '__main__':
   summary()
