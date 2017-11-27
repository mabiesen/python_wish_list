## should allow for pulling all classnames from scripts
## option to pull all methods

## should allow for pulling all function initiations

## should allow for pulling all global variables
## option to count number of global variables

## move through all files in directory and perform one or more of the above operations

## SHOULD BE A CLI BASED TOOL WITH PRINT OUTPUT.


import click
from disectScriptFunctionality import main_func

@click.command()
@click.option('--file', help='python file to dissect')
def summary(file):
    main_func(file)

if __name__ == '__main__':
   summary()
