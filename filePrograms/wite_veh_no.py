vehicle_numbers=["KL04AR5418","KL04AP8415,KL07AB4334"]

f=open("C:\\Users\\aseed\\OneDrive\\Desktop\\PythonJune\\filePrograms\\veh_no.txt","w")

for num in vehicle_numbers:

    f.write(num+"\n")