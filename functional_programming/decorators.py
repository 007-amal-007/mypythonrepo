def revert_val(func):
    def wrapper(no1,no2):
        if no1<no2:
            (no1,no2)=(no2,no1)
            return func(no1,no2)
        else:
            return func(no1,no2)
    return  wrapper

@revert_val
def sub(no1,no2):
    return (no1 - no2)
print(sub(1,10))

@revert_val
def div(num1,num2):
    return num1/num2
print(div(2,10))