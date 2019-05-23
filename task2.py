from task1 import L33t
import os

# get the dictionary for the files 
myval=os.system("ls -l| awk \'{print $9}\'  ")
mykey=os.system("pwd")
mydic={}
mydic[mykey]=myval
print(mydic)


#get the length of the string
for var in myval:
	mylst[var]= len(var)

