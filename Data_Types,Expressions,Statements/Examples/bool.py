#using bool() function
# 0,empty string and empty data types are considered as false
# non-zero numbers, non-empty string and non-empty datatypes are considered as true

a=0
print(bool(a))
b='Life'
print(bool(b))
a=''
print(bool(a))
c=2+9j
print(bool(c))
b=0+0j
print(bool(b))
print(bool(True))
print(bool(False))
a=2
b=3
print("Is 2 > 3 ",bool(a>b)) # can apply relational operation within bool function
print("Is 2 != 3 ",bool(a!=b))
print("Is 2 == 3",bool(a==b))