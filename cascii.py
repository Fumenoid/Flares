#!/usr/bin/python3
#A program for ASCII conversion.
#Arguments type - Command line.
#Author - Fumenoid. 
#comments - :Firebelly:

import argparse 


parser = argparse.ArgumentParser(description='This script is used to convert a letter to it\'s ASCII code or ASCII code to it\'s respective letter')
parser.add_argument('-n', '--number', type=str, help='use this argument to pass ascii value, Note: for mutilple values use -` "65 66 67 68" `.')
parser.add_argument('-s', '--string', type=str, help='use this argument to pass string, Note: Space bar in string will also be converted to ascii code.')
args=parser.parse_args()

if __name__ == '__main__':
	if((args.number==None and args.string==None) or (args.number!=None and args.string!=None)):
		print("Invalid Arguments... :(\n")
	elif (args.string==None):
		templist=list(args.number.split(" "))
		alphalist=[]
		for i in range(len(templist)):
			alphalist.append(chr(int(templist[i])))
		print(''.join(alphalist))
	else:
		numberlist=[]
		for i in range(len(args.string)):
			numberlist.append(str(ord(str(args.string[i]))))
		print(' '.join(numberlist))