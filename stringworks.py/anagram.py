sourse_word="listen"

target_word="silent"

sorted_sourse_word=sorted(sourse_word)

sorted_target_word=sorted(target_word)

print(sorted_sourse_word==sorted_target_word)


#---------------------------------------------------#
#using 

def is_anagram(word1,word2):

    return sorted(word1)==sorted(word2)

sourse_word="silent"

target_word="listen"


