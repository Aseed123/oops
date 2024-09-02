
list=[2,4,6,8,10,3,5,7,9]
odd_count=0
even_count=0
for i in list:
    if(i%2==0):
        even_count=even_count+1
    else:
        odd_count=odd_count+1
print(f"count of even = {even_count}\ncount of odd = {odd_count}")