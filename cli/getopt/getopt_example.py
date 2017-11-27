import getopt
import sys

def command_line_arguments():
    print 'ARGV      :', sys.argv[1:]

    options, remainder = getopt.getopt(sys.argv[1:], 'r:s:d', ['requestlist','send','delete'])
    for opt, arg in options:
        if opt in ('-r', '--requestlist'):
            option = "request"
            print(option)
            print(arg)

        elif opt in ('-s', '--send'):
            option = "send"
            print(option)
            print(arg)

        elif opt in ('-d', '--delete'):
            option = "delete"
            print(option)
            print(arg)

command_line_arguments()
