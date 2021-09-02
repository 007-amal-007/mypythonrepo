#key:value pair
#keys are always unique
#value can repeat\duplicate
#all keys are in same type in a dictionary
#keys=homo    values=hetero
#mutable

#nesting possible
d={1:"hello",2:{2:3,4:6}}
print(d)


dict={'name':'zara','age':7,'class':'first'}
print(dict)

print(type(dict))

print(dict['name'])

print("dict['name']:",dict['name'])
print("dict['age']:",dict['age'])

dic={}  #empty dictionary
# print(dic)
# print(type(dic))

dict['age']=8  #update
# print(dict)

dict['school'] = "ptmhss school"  # 1st type #add
dict.update({'location':'tkd'})   # 2nd
# print(dict)

del dict['name']   #remove entry with key 'name'
dict.clear()       #remove all entries in dict
del dict           #delete including dict
# print(dict)


a="hello,world"  #to split words
c={}
b=a.split(",")
print(b)         #we get the answer in list
for i in b:
    print(i)