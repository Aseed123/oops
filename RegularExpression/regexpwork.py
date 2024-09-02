from re import finditer

text="aseedabidaseedabidaseed"

matcher=finditer("aseed",text)

count=0

for m in matcher:


    print(m.start(),"===",m.group())

    count+=1

print(count)

