data = input()
a = int(data[0])
b = int(data[1])
c = int(data[2])

if (a >= b and a <= c) or (a <= b and a >= c):
    print (a)
elif (b >= a and b <= c) or (b <= a and b >= c):
    print (b)
else:
    print(c)