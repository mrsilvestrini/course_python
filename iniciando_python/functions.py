def call_numbers():
    for number in range(0,10):
        print(number)

def call_numbers_with_limit(limit):
    list=range(0,10)
    for number in range(limit) :
        print(number)

#call_numbers()
call_numbers_with_limit(5)

def sum(x=0,y=0):
    return x+y

def sub (x=0,y=0):
    return x-y

def mult (x=0,y=0):
    return x*y

def div (x,y):
    if(y<1):
        return 0
    return x/y

print(sum(x=10,y=7))
print(sum())

print(div(x=-1,y=0))
print(div(x=50,y=3))

