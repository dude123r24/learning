#!/usr/bin/env Python3

print ("Hello World")

txt="""    amit,likes coding.
He loves to learn new things.    """

print () # prints blank line
print ("+++ Strings +++\n")
print ("\ntxt : " + txt +"\n")

print ("Strings split : txt.split(',') : " + str(txt.split(",")) + "\n") # Can only concatenate list if cast into str :)

print ("Strings are arrays : txt[1] : " + txt[1] + "\n") # strings are arrays

print ("Slicing : txt[-4:-1] : " + txt[-4:-1] + "\n") #slicing
# print (txt[-4:-9]) #slicing # Does not work! Why?

print (str(len(txt)) + "\n") # Cannot concatenate number unless cast into string

print ("txt.strip() : \nWithout : " + "'" +txt + "'" +"\n\nWith : " + "'" + txt.strip() + "'" + "\n") # To remove spaces before and after

# Search replace multiple items. For single items its single just use txt.replace(i, j)
print ("Search replace multiple items: " + "\n")
dic={"amit": "Sejal", "He": "She"}
for i, j in dic.items():
  txt = txt.replace(i, j)
  print(txt)
print("\n" + txt + "\n")


print (".format usage")
sentence="amit loves {loves}, and hates {hates}".format(loves="peaches", hates="politics")
print (sentence+ "\n")


print ("index usage : sentence.index()")
p=print (sentence.index("peach"))


import subprocess
import sys

cmdping = "ping -c4 www.cyberciti.biz"
p = subprocess.Popen(cmdping, shell=True, stderr=subprocess.PIPE)
while True:
    out = p.stderr.read(1)
    if out == '' and p.poll() != None:
        break
    if out != '':
        sys.stdout.write(str(out))
        sys.stdout.flush()

print("\n" + "Return Code: " + p.returncode + "\n")
