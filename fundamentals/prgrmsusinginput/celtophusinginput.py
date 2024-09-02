#write a program to convert temperature format in degree celcious to farahnheat

temp_in_degreecelsious=int(input("Enter the temperatue in celcious:"))

temp_in_ph=((9/5)*temp_in_degreecelsious)+32

print(f"fh temperature = {temp_in_ph}") 