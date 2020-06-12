#1
# a = 777
# b = 777
# print(a == b, a is b)
#3
a=3.5
b=int(3.5)

print(a**((a//b) * 2))
print(((a-b)*a)//b)
b=(((a-b)*a)%b)
print(b)
print( (a * 4) % ( b * 4 ) )

a=10.6
b=10.5
print(a*b)
print(type(a+b))

a="3.5"
b=4
print(a*b)
a="3.5"
b="1.5"
print(a+b)

a='3'
b=float(a)
print(b ** int(a))

a=20
b=4
print(type((a / b)))