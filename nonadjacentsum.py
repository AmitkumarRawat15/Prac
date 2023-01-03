inputlist = [-2,1,3,-4,5]
a = 0
b = 0
for i in inputlist:
    if b>a:
        new_b = b
    else:
        new_b = a
    a = b+i
    b = new_b

if b>a:
    print(b)
else:
    print(a)