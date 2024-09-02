
f=open("C:\\Users\\aseed\\OneDrive\\Desktop\\PythonJune\\filePrograms\\news.text","r")

word_list=[]

# for line in f:
 
#     word=line.rstrip("\n")

#     word=word.split(" ")

    # for w in word:

    #     word_list.append(w)
word_list=[w for line in f for w in line.rstrip("\n").split(" ")if  w!=""]

word_count={w:word_list.count(w) for w in word_list}


def get_value(key):

    return word_count.get(key)

srt=sorted(word_count,key=get_value,reverse=True)

print(srt)