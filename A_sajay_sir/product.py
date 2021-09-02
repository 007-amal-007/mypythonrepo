products=[
    {"p_name":"complan","mrp":230,"avl_qty":50},
    {"p_name": "horlicks", "mrp": 250, "avl_qty": 10},
    {"p_name": "bournvita", "mrp": 220, "avl_qty": 0},
    {"p_name": "nutricharge", "mrp": 200, "avl_qty": 100},
    {"p_name": "mylo", "mrp": 100, "avl_qty": 0},

]
#print all product names in the shop
# MAP
product_names=list(map(lambda item:item["p_name"],products))
print(product_names)

#print all produvts available in the shop
#FILTER
# aval_product=list(filter(lambda item:item["avl_qty"]>0,products))
# print(aval_product)
#
# #print out of stock product
# out_stock=


#low cost product
from functools import reduce
prices=list(map(lambda price:price["mrp"],products))
print(prices)
print(min(prices))