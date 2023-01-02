def sum(a,b):
    sum = a + b
    print("sum : " + str(sum))

def mul(a,b):
    sum = a * b
    print("mul : " + str(sum))

def greeting(callback):
    a = 10
    b = 5
    callback(a,b)


greeting(sum)
greeting(mul)