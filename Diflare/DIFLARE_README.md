# DiFlare
---

A python script that show the files that have been modified/changed/removed in two different folders or if two files differ.

Possible use case, to check which files have been modified/differ in two different versions of a project/software or if two files differ or not(can be used to check if files have been tampered).

##### Diflare help
```
./diflare.py -h
usage: diflare.py [-h] [-p1 PROJECTONE] [-p2 PROJECTTWO]

Find files that differ between two folders/projects

optional arguments:
  -h, --help            show this help message and exit
  -p1 PROJECTONE, --projectone PROJECTONE
                        Pass the project folder one address, please give full path
  -p2 PROJECTTWO, --projecttwo PROJECTTWO
                        Pass the project folder two address, please give full path
```
---
##### Diflare Example usage

```
./diflare.py -p1 Testprojectv1/ -p2 Testprojectv2 

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
---

##### Fail Condition
In case of MD5 collision which is very unlikely to happen in some real life project.