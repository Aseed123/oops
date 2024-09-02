#numbers=[1,2[3,(100,200,300),4],5,6] >>> [1,2[3,4,(100,150,200,300)],5,6]

numbers=[1,2,[3,(100,200,300),4],5,6]  

num=numbers[2][1]  

new_num=list(num)  

new_num.append(150)  

new_num.sort()

numbers[2][1] = tuple(new_num)  

n=numbers[2].pop()

numbers[2].insert(1,n)


print(numbers)