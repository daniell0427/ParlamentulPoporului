from database import select

a=select('549')
b=a[0][0]
c=a[0][1]
d=a[0][2]
print(b)
print(c)
print(d)
