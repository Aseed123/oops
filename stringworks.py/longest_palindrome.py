
#using i,left,right,longest_palindrome,current_palindrome

text="RACECAR"

longest_palindrome=""

for i in range(0,len(text)):

    right=i

    left=i

    while (left >=0 and right<len(text) and text[left] == text[right]):

        current_palindrome_text=text[left:right+1]

        if len(current_palindrome_text)>len(longest_palindrome):

            longest_palindrome=current_palindrome_text

        left-=1

        right+=1

print(longest_palindrome)
