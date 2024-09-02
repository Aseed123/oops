
from json import load

f=open("C:\\Users\\aseed\\OneDrive\\Desktop\\PythonJune\\jsonWorks\\products.json",encoding="UTF-8")

products=load(f)

#print(len(products))

product_titles=[p.get("title")for p in products]

# print(product_titles)

jwelery_products=[p.get("title") for p in products if p.get("category")=="jewelery"]

# print(jwelery_products)

above_100_products=[p.get("title")for p in products if p.get("price")>100]

# print(above_100_products)

#q products available in range of 100 and 150

range_100and150_products=[p.get("title")for p in products if  p.get("price")in range(100,151)]

range_100and150_products=[p.get("title")for p in products if  p.get("price")<=100 and p.get("price")<=150]

# print(range_100and150_products)

#products with most number of rating

def get_rating_count(dic):

    return(dic).get("rating").get("count")

top_selling_product=max(products,key=get_rating_count)

print(top_selling_product)
