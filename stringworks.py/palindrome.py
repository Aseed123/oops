#longest palindromic substring from the given string

# String-RACECAR

#R
#A
#CEC
#ACECA
#RACECAR

text="RACECAR"

for i in range(len(text)):

    left=i

    right=i

    while(left >=0 and right<len(text) and text[left] == text[right] ):

        current_palindrome=text[left:right+1]

        print(current_palindrome)

        left=left-1

        right=right+1