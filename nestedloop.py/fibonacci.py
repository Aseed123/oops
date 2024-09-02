#fibonaxxi series

#0 1 1 2 3 5 8 13 21


previous=0

current=1

print(f"{previous},{current}",end=",")

for i in range(1,11):

    next=previous+current

    print(f"{next}",end=",")

    previous=current

    current=next
