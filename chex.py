#!/usr/bin/python3
#A program for ASCII conversion.
#Arguments type - Command line.
#Author - Fumenoid. 
#comments - :nukedom:
#string to hex - " bytes.hex(b'crypto') or bytes.hex(str.encode(args.string)) "
#hex to string - " bytes.fromhex(args.hexadecimal).decode('utf-8') "

import argparse
parser = argparse.ArgumentParser(description='This script is used to convert a letter to it\'s ASCII code or ASCII code to it\'s respective letter')
parser.add_argument('-hex', '--hexadecimal', type=str, help='use this argument to pass hex and decode it into utf-8.')
parser.add_argument('-s', '--string', type=str, help='use this argument to pass string and encode it into hexadecimal.')
args=parser.parse_args()

if __name__ == '__main__':
	if((args.hexadecimal==None and args.string==None) or (args.hexadecimal!=None and args.string!=None)):
		print("Invalid Arguments... :(\n")
	elif (args.string==None):
		print(bytes.fromhex(args.hexadecimal).decode('utf-8'))
	else:
		print(bytes.hex(str.encode(args.string)))