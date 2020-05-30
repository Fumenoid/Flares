#!/bin/python3
# Author - Fumenoid
# A script that show files that differ between two folders/or if two files differ.
# Fail case - In case on MD5 collision (which i very unlikely to happen in real world projects)
import subprocess
import argparse 
from termcolor import colored, cprint

parser = argparse.ArgumentParser(
    description='Find files that differ between two folders/projects'
    )
parser.add_argument(
    '-p1',
    '--projectone',
    type=str, 
    help='Pass the project folder one address, please give full path'
    )
parser.add_argument(
    '-p2',
    '--projecttwo',
    type=str,
    help='Pass the project folder two address, please give full path'
    )
args=parser.parse_args()

def findfiles(foldername):
    result = subprocess.run(["find", foldername,"-type","f"], shell=False, capture_output=True)
    listoffiles = str(result.stdout)[2:-3].split('\\n')
    return listoffiles

def md5(listfiles):
    dictionary = {}
    for elem in listfiles:
        result = subprocess.run(["md5sum", elem], shell=False, capture_output=True)
        dictionary.setdefault(str(result.stdout)[2:-3].split('  ')[0], str(result.stdout)[2:-3].split('  ')[1])
    return dictionary

if __name__ == "__main__":
    #banner starts
    cprint('\n\t    (                                      ', 'yellow', attrs=['bold'])
    cprint('\t    )\ )      (     (     (                ', 'yellow', attrs=['bold'])
    cprint('\t   (()/(  (   )\ )  )\ )  )\    )  (      (', 'yellow', attrs=['bold'])
    cprint('\t  /(_)) )\ (()/( (()/( ((_)( /(  )(    ))\ ', 'red', attrs=['bold'])
    cprint('\t  (_))_ ((_) /(_)) /(_)) _  )(_))(()\  /((_)', 'red', attrs=['bold'])
    cprint('\t  |   \ (_)(_) _|(_) _|| |((_)_  ((_)(_)) ', 'white', attrs=['bold'])
    cprint("\t  | |) || | |  _| |  _|| |/ _` || '_|/ -_)", 'white', attrs=['bold'])
    cprint('\t  |___/ |_| |_|   |_|  |_|\__,_||_|  \___|', 'white', attrs=['bold'])
    cprint("\n\t\t\t\t\t by @fumenoid", 'white', attrs=['bold'])
    cprint("\t\t\t\t\t https://github.com/Fumenoid\n", 'white', attrs=['bold'])
    #banner ends
    if args.projectone==None or args.projecttwo==None:
        cprint(
            "[-] Invalid arguments passed D:\n",
            'yellow'
            )
        exit()
    else:
        try:
            fileinf1 = findfiles(args.projectone)
            fileinf2 = findfiles(args.projecttwo)
            dict1 = md5(fileinf1)
            dict2 = md5(fileinf2)
            cprint(
                "Analysing files....\n",
                'yellow',
                attrs=['bold']
                )
            cprint(
                f"{args.projectone} has {len(dict1.keys())} files.",
                'red',
                attrs=['bold']
                )
            cprint(
                f"{args.projecttwo} has {len(dict2.keys())} files.\n",
                'red',
                attrs=['bold']
                )
            cprint(
                f"Reference using {args.projectone}",
                'yellow',
                attrs=['bold']
                )
            cprint(
                f"It means project one will be compared to project two and differences will be noted\n",
                'yellow',
                attrs=['bold']
                )
            for ha in dict1.keys():
                if ha not in dict2.keys():
                    cprint(f"[+] {dict1[ha]} present in {args.projectone} got modified/removed in {args.projecttwo}", 'red', attrs=['bold'])
                else:
                    if dict2[ha].split('/')[-2] != dict1[ha].split('/')[-2] :
                        cprint(
                            f"[+] File '{dict1[ha].split('/')[-1]}' present in both files but in different directories.."
                            f"\n\tIn {args.projectone} at {dict1[ha]}\n\tIn {args.projecttwo} at {dict2[ha]}",
                            'red',
                            attrs=['bold']
                            )
            cprint(
                f"\nReference using {args.projecttwo}",
                'yellow',
                attrs=['bold'])
            cprint(
                f"It means project two will be compared to project one and differences will be noted\n",
                'yellow',
                attrs=['bold']
                )
            for idd in dict2.keys():
                if idd not in dict1.keys():
                    cprint(
                        f"[+] {dict2[idd]} present in {args.projecttwo} got modified/removed in {args.projectone}",
                        'red',
                        attrs=['bold']
                        )
                else:
                    if dict2[idd].split('/')[-2] != dict1[idd].split('/')[-2] :
                        cprint(
                            f"[+] File '{dict1[idd].split('/')[-1]}' present in both files but in different directories.."
                            f"\n\tIn {args.projectone} at {dict1[idd]}\n\tIn {args.projecttwo} at {dict2[idd]}",
                            'red',
                            attrs=['bold']
                            )
            cprint(
                "\ndone... bye\n",
                'yellow',
                attrs=['bold']
                )
        except:
            cprint(
                "Invalid path/paths or Folder doesn't exists....\nPlease provide full path from root directory or both folders should be in present working directory"
                f"\nUse any of these formats when giving paths of folders"
                f"\n\n-> (./foldername) or (/home/ubuntu/foldername)\n",
                'yellow',
                attrs=['bold']
            )