num = 5

s = 0

for i in range(1,num+1):
    s += i
    if (num == i):
        print(i,end = "=")
        print(s)
    else:
        print(i,end = "+")

p = 1

for i in range(1,num+1):
    p *= i
    if (num == i):
        print(i,end = "=")
        print(p)
    else:
        print(i,end = "*")