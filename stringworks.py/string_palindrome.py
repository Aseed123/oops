#create a function is_palindrome(word) return True if word is a palindromic string
#else return False

def is_palindrome(word):

    rev_word=word[::-1]

    return word==rev_word

print(is_palindrome("malayalam"))

