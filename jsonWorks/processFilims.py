
from json import load

f=open("C:\\Users\\aseed\\OneDrive\\Desktop\\PythonJune\\jsonWorks\\filims.json","r")


films=load(f)

for m in films:

    print(m.get("title"))