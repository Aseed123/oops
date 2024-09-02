from re import finditer

text="ab d123 @#7L,Mdef"

# pattern="[abd]"  #check for a ,b ,or d

# pattern="[a-k]"    #check for letters from a to k (all lowercase)

# pattern="[A-Z]"     #check for letters from A to Z (all Uppercase)

# pattern="[a-zA-Z]" #check for All letters both Uppercase and lowercase 

# pattern="[0-9]"    #check for digits

# pattern="[a-zA-Z0-9]"  #check for all alphanumerics charecters

# pattern="[^a-zA-Z0-9]"   #check for all speacial characters(exclude a-z,A-Z,0-9)

# pattern="[\s]"   #check for space

# pattern="[^a-zA-Z0-9\s]"


matcher=finditer(pattern,text)

for m in matcher:

    print(m.start(),"===",m.group())

