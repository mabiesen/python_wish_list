import getopt
import sys

def command_line_arguments():
	print 'ARGV      :', sys.argv[1:]

	options, remainder = getopt.getopt(sys.argv[1:], 'r:s:d', ['requestlist',
	                                                         'send',
	                                                         'delete',
	                                                         ])
	print('OPTIONS   :' + options)
	for opt, arg in options:
		if opt in ('-r', '--requestlist'):
			#mylist = util_message.get_user_input("Please provide the name of the list you would like to see: ")
			option = "request"
			print(option + ":" + arg)

		elif opt in ('-s', '--send'):
			#mylist = util_message.get_user_input("Please provide the name of the list you would like to add to: ")
			option = "send"
			print(option + ":" + arg)

		elif opt in ('-d', '--delete'):
			#mylist = util_message.get_user_input("Please provide the name of the list you would like to add to: ")
			option = "delete"
			print(option + ":" + arg)

command_line_arguments()
