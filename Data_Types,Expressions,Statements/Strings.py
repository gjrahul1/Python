Str="Z"
#ord() returns unicode value for single character String
ascii_num=ord(Str)
print("The value of unicode of "+Str+" is :",ascii_num)

#chr() returns single character String for unicode value
print("Unicode of 65 is :",chr(88))

#capitalize() : capitalizes first single character in string
Str="apple"
cap=Str.capitalize()
print("Captialized "+Str+" =",cap)

#upper() : used to capitalize entire string
up=Str.upper()
print("Upper String of "+Str+" is "+up)

#len : finds the length of the given string
print("Length of given string:",len(Str))

#Practice Question

#QUESTION 1
""" Create a output like

1.Race
2.GAME
3.lIFE
4.It is lie
from the given Str String

*don't create them
"""

Str = 'Life is not a race or game, it is lie'
v1=Str[14:18] #race
p1=v1.title() #If string is sliced, the capitalize() function wouldn't work. title() will work.
print(p1)
v2=Str[22:26] #game
p2=v2.upper()
print(p2)
v3=Str[0:4] #life
v3=v3.lower()
t1=v3[0] #l
t2=v3[1:4] #ife
t2=t2.upper()
p3=t1+t2
print(p3)
v4=Str[28:38] #It is lie
p4=v4.capitalize()
print(p4)
