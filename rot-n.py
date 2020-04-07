#!/usr/bin/python3
#A program for ROT-N decryption.
#Arguments type - Command line.
#Author - Fumenoid. 
#comments - :SoulHeart:

import argparse
import re

alcaps="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alsmal="abcdefghijklmnopqrstuvwxyz"
parser = argparse.ArgumentParser(description='This is ROT-N code that tries to all rot combination to find the flag for a challenge')
parser.add_argument('-n', '--number', type=int, help='supply rot number')
parser.add_argument('-s', '--string', type=str, help='supply string')
parser.add_argument('-b', '--brute', type=str, help='pass "-b Y" to brute force rot')
parser.add_argument('-f', '--file', type=str, help='supply file to read data')
parser.add_argument('-ff', '--flagformat', type=str, help='supply flag format to search flag')
args=parser.parse_args()
def rotfun(n, string):
	rstring=''
	for i in range(len(string)):
		if string[i].islower():
			index=alsmal.find(string[i])
			rstring=rstring+alsmal[(index+n)%26]
		elif string[i].isupper():
			index=alcaps.find(string[i])
			rstring=rstring+alcaps[(index+n)%26]
		else:
			rstring=rstring+string[i]
	return rstring

if __name__ == '__main__':
	if((args.file==None and args.string==None) or (args.file!=None and args.string!=None)):
		print("Invalid Input Source.. Argument error")
		exit()
	else:
		if(args.file!=None):
			with open(args.file, 'r') as f:
				stringer=f.read()
		else:
			stringer=args.string+'\n'
	if(args.brute==None):
		rstr=rotfun(args.number, stringer)
		print("Rot-"+str(args.number)+", string->\n"+rstr)
	else:
		if(args.flagformat==None):
			print("Brute-forcing using keys 1-25\n")
			for i in range(26):
				rstr=rotfun(i, stringer)
				print("Rot-"+str(i)+", string->\n"+rstr)
		else:
			print("Searching flagformat "+args.flagformat)
			for i in range(26):
				rstr=rotfun(i, stringer)
				if(re.search(args.flagformat, rstr)!=None):
					print("Key-"+str(i)+", string->\n"+rstr)
					exit()
			print("Cant find flag, try Brute-forcing without it!")


			
