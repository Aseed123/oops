
arr=[ [10,20] , [21,30] , [40,50] ]

evens=[]

for lst in arr:

    for num in lst:

        if num%2==0:
            
            evens.append(num)

print(evens)


#method 2

arr=[ [10,20] , [21,30] , [40,50] ]

evens=[num for lst in arr for num in lst if num%2==0]

print(evens)