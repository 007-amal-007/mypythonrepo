#loca variable can only used inside the function.
#but we define the variable globally it can use both inside and outside of the function.

x=5

def foo():
    global x
    x=x+10
    print("local x:",x)

foo()
print("global x:",x)

#we can define more variables inside "global" by using " , "
#
# x=3
# y=5
#
# def global():
#     global x,y
#     a=x**2
#     b=x*y
#     print("")