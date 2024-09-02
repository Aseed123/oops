#sum of odd numbers in between 1 to 100

i=1

total=0

while(i<=100):
    if (i%2!=0):
        total=total+i
    i=i+1
print(f"Sum={total}")