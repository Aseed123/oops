
from re import finditer

text="abc 7Klef85  g@#"

#pattern="\d"   #[0-9]
# pattern="\D"  #[^0-9]
# pattern="\w"  #[a-zA-Z0-9]
# pattern="\W"    #[^a-zA-Z0-9]
# pattern="\s"    #space
# pattern="\S"    #Exclude space


matcher=finditer(pattern,text)

for m in matcher:

    print(m.start(),"==",m.group())