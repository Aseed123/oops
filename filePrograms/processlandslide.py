
f=open("C:\\Users\\aseed\\OneDrive\\Desktop\\PythonJune\\filePrograms\\landslide.txt","r")

data=[]

for line in f:#kerala 2018 14
   
    lst=line.rstrip("\n").split(" ")#["kerala","2018",14]

    dic={"state":lst[0],"year":lst[1],"deaths":int(lst[2])}

    data.append(dic)

# print(data)

#q1  print states and total death rates

state_summary={}

for dic in data:

    state=dic.get("state")

    death_count=dic.get("deaths")

    if state in state_summary:

        state_summary[state]+=death_count

    else:

        state_summary[state]=death_count

print(state_summary)


    