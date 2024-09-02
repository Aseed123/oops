#odd numbers in between starting limit and ending limmit

start_limit=int(input("Enter the Starting number : "))

end_limit=int(input("Enter the ending number : "))
                    
while(start_limit<=end_limit):
    if (start_limit%2!=0):
        print(start_limit)
    start_limit=start_limit+1