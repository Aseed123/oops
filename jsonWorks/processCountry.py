#q1  print all the country in the list
#q2  total number of country
#q3  country with same languages
#q4  highest populated country
#q5  largest country
#q6  smallest country
#q7  currency of Vietnam
#q8  non independent countries
#q9  populations below 200000
#q10 Uzbekistan is independent or not
#q11 countries and their callingcodes
#q12 numeric code of United States
#q13 native name of Hungary
#q14 country have most timezone
#q15 capital of Russian Federation

from json import load

f=open("C:\\Users\\aseed\\OneDrive\\Desktop\\PythonJune\\jsonWorks\\country.json",encoding="UTF-8")

data=load(f)



all_name=[c.get("name")for c in data]

#print(all_name)

#print(len(data))

region_summary={}

for c in data:

    region_name=c.get("region")

    if region_name in region_summary:

        region_summary[region_name]+=c.get("area",0)
    else:
        region_summary[region_name]=c.get("area",0)

#print(region_summary)

value_key=[(v,k) for k,v in region_summary.items()]

print(max(value_key))