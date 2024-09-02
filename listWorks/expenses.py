expenses=[120000,130000,110000,150000,210000,130000,280000]

#find count of object in expenses

expense_count=len(expenses)

#print expense count

#print all expenses

for i in range(0,expense_count):

    print(expenses)

#print expense>15000

for i  in range(0,len(expenses)):

    if expenses[i]>150000:
        print(expenses[i])

#print total expense

total_expense=0

for i in range(0,len(expenses)):

    total_expense=total_expense+expenses[i]

print(total_expense)



#print average expense

average_expense=total_expense/len(expenses)

print(average_expense)