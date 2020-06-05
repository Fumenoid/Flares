# Flares
CLI tools to help me in CTF's

---
### Rot-N tool
---

It is basically a ceasor cipher tool which either encrypt/decrypt data either supplied as argument or in a file, this tool can also use to brute force for all 1-25 keys, you can use brute force mode to display all possible rot-n forms or to find a string which match the flag format.

- ##### To use 
```
$ git clone https://github.com/Fumenoid/Flares.git
$ chmod +x rot-n.py
$ ./rot-n.py -h
```
- ##### Rot-n Help
```
$ ./rot-n.py -h
usage: rot-n.py [-h] [-n NUMBER] [-s STRING] [-b BRUTE] [-f FILE] [-ff FLAGFORMAT]

This is ROT-N code that tries to all rot combination to find the flag for a challenge

optional arguments:
  -h, --help            show this help message and exit
  -n NUMBER, --number NUMBER
                        supply rot number
  -s STRING, --string STRING
                        supply string
  -b BRUTE, --brute BRUTE
                        pass "-b Y" to brute force rot
  -f FILE, --file FILE  supply file to read data
  -ff FLAGFORMAT, --flagformat FLAGFORMAT
                        supply flag format to search flag
```

- ##### Example Usage
```
$ ./rot-n.py -n 13 -s "Jbnj, n fvzcyr ebg13 ntnva"
Rot-13, string->
Woaw, a simple rot13 again

$ ./rot-n.py -b Y -ff ctf{.*} -s "sjv{1_qc_q_Vbqw}"
Searching flagformat ctf{.*}
Key-10, string->
ctf{1_am_a_Flag}

```

##### Note : The tools shows all the output on terminal, you can redirect the output to a file, if the input string or file is too big. 

---

### CASCII
---

This script is used to convert a letter to it's ASCII code or ASCII code to it's respective letter

- ##### To use
```
$ git clone https://github.com/Fumenoid/Flares.git
$ chmod +x cascii.py
$ ./cascii.py -h
```

- ##### Cascii Help
```
$ ./cascii.py -h
usage: cascii.py [-h] [-n NUMBER] [-s STRING]

This script is used to convert a letter to it's ASCII code or ASCII code to it's respective letter

optional arguments:
  -h, --help            show this help message and exit
  -n NUMBER, --number NUMBER
                        use this argument to pass ascii value, Note: for mutilple values use -` "65 66 67 68" `.
  -s STRING, --string STRING
                        use this argument to pass string, Note: Space bar in string will also be converted to ascii code.
```
- ##### Example Usage
```
$ ./cascii.py -s "Hey, it's Fume"
72 101 121 44 32 105 116 39 115 32 70 117 109 101

$ ./cascii.py -n "72 101 121 44 32 105 116 39 115 32 70 117 109 101"
Hey, it's Fume
```
---

### Chex
---

This script is used to convert a ascii string to hex, or hex back to ascii string

- ##### To use
```
$ git clone https://github.com/Fumenoid/Flares.git
$ chmod +x chex.py
$ ./chex.py -h
```

- ##### CHex Help
```
$ ./chex.py -h
usage: chex.py [-h] [-hex HEXADECIMAL] [-s STRING]

This script is used to convert a ascii string to hex, or hex back to ascii string

optional arguments:
  -h, --help            show this help message and exit
  -hex HEXADECIMAL, --hexadecimal HEXADECIMAL
                        use this argument to pass hex and decode it into utf-8.
  -s STRING, --string STRING
                        use this argument to pass string and encode it into hexadecimal.
```
- ##### Example Usage
```
$ ./chex.py -s "Hey, it's Fume"
4865792c20697427732046756d65

$ ./chex.py -hex "4865792c20697427732046756d65"
Hey, it's Fume
```

---


### DiFlare
---

A python script that show the files that have been modified/changed/removed in two different folders or if two files differ.

Possible use case, to check which files have been modified/differ in two different versions of a project/software or if two files differ or not(can be used to check if files have been tampered).
- ##### To use
```
$ git clone https://github.com/Fumenoid/Flares.git
$ cd Diflare
$ chmod +x diflare.py
$ ./diflare.py -p1 <pathofprojectone> -p2 <pathofproject2>
```
- ##### Diflare Help
```
$ ./diflare.py -h
usage: diflare.py [-h] [-p1 PROJECTONE] [-p2 PROJECTTWO]

Find files that differ between two folders/projects

optional arguments:
  -h, --help            show this help message and exit
  -p1 PROJECTONE, --projectone PROJECTONE
                        Pass the project folder one address, please give full path
  -p2 PROJECTTWO, --projecttwo PROJECTTWO
                        Pass the project folder two address, please give full path
```

- ##### Diflare Example usage

```
$ ./diflare.py -p1 Testprojectv1/ -p2 Testprojectv2 

            (                                      
            )\ )      (     (     (                
           (()/(  (   )\ )  )\ )  )\    )  (      (
          /(_)) )\ (()/( (()/( ((_)( /(  )(    ))\ 
          (_))_ ((_) /(_)) /(_)) _  )(_))(()\  /((_)
          |   \ (_)(_) _|(_) _|| |((_)_  ((_)(_)) 
          | |) || | |  _| |  _|| |/ _` || '_|/ -_)
          |___/ |_| |_|   |_|  |_|\__,_||_|  \___|

                                         by @fumenoid
                                         https://github.com/Fumenoid

Analysing files....

Testprojectv1/ has 5 files.
Testprojectv2 has 6 files.

Reference using Testprojectv1/
It means project one will be compared to project two and differences will be noted

[+] Testprojectv1/file present in Testprojectv1/ got modified/removed in Testprojectv2
[+] File 'iop' present in both files but in different directories..
        In Testprojectv1/ at Testprojectv1/tria/iop
        In Testprojectv2 at Testprojectv2/iop
[+] Testprojectv1/tria/poi/opse present in Testprojectv1/ got modified/removed in Testprojectv2

Reference using Testprojectv2
It means project two will be compared to project one and differences will be noted

[+] Testprojectv2/tria/poi/opse present in Testprojectv2 got modified/removed in Testprojectv1/
[+] Testprojectv2/file present in Testprojectv2 got modified/removed in Testprojectv1/
[+] File 'iop' present in both files but in different directories..
        In Testprojectv1/ at Testprojectv1/tria/iop
        In Testprojectv2 at Testprojectv2/iop
[+] Testprojectv2/newfile present in Testprojectv2 got modified/removed in Testprojectv1/

done... bye

```

- ##### Fail Condition of Diflare
In case of MD5 collision which is very unlikely to happen in some real life project.

---
