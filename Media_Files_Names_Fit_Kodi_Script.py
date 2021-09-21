import os
import re
import string

dirpath=os.getcwd()

files=os.listdir(dirpath)

seasonNum=''
def getSeasonNumber():
    global seasonNum
    print("Enter Season Number:")
    seasonNum=input()

getSeasonNumber()
while not seasonNum.isdigit():
    print("Note: You must enter a number.")
    getSeasonNumber()



convert = lambda text: int(text) if text.isdigit() else text
alphanum_key = lambda key: [convert(c) for c in re.split('([0-9]+)', key)]

for file in sorted(files,key=alphanum_key):
    print(file)

isRename=''

while isRename not in ['y','n']:
    print("Do you want to auto rename files as above order (y/n): ")
    isRename=input()

if isRename=='n':
    exit(0)

print("\n\n-----\tResult\t-----\n\n")
filesSorted=sorted(files,key=alphanum_key)
filesCounter=len(filesSorted);
for file in reversed(filesSorted):
    filename, file_extension=os.path.splitext(file)
    result="S"+ ('%2d' % int(seasonNum)).replace(" ","0") +"E"+('%2d' % filesCounter).replace(" ","0")+file_extension
    filesCounter-=1
    os.rename(file, result)
    print(result)
print("\n\n-----\tSuccessful\t-----\n\n")