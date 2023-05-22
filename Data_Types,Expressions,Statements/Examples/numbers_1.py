num1,num2,num3=5,6.5321,7+2j
print("Integer=",num1)
print("Float=",num2)
print("Complex Number=",num3)
temp=num1+num3 #only the real part of the equation gets added
print(temp)
temp=num2*num3 #both the real and imaginary part of the equation is multiplied
print(temp)

#abs - returns absolute value of a number
print("Printing absloute value of the %d number"%num1)
print(abs(num1))

#round - rounds the number to the given decimal value if any else returns whole number
q=temp=round(num2,2)
print("Rounding %d to 2 decimal places"%num2)
print(temp)

#pow - returns the power of given integer number
print("Power of 5 raised to 2 is",pow(5,2))

#min = returns minimum of given numbers
temp=min(temp,num1,3)
print("The minimum value among "+str(q)+" ,"+str(num1)+" ,"+"3 is ",temp)

#max - returns maximum value out of the given numbers
temp=max(temp,num1,4)
print("The maximum value among "+str(q)+","+str(num1)+","+"4 is",temp)

#divmod - returns quotient and reminder
temp=divmod(temp,num1)
print("Quotient and Reminder of 5 and 5 is",temp)
#output ia (1,0) where 1 is quotient and 0 is reminder

'''
Perform the following operations and print them :

Create a number 112 and store it in num1 variable
Create a number 20.45 and store it in num2 variable
Create a number 7 + 3j and store it in num3 variable
Print the sum of the numbers
Print the product of num2 and num3 and also store it in num4 variable
The remainder when num1 is divided by num2 and round off it to 2 decimal places
The imaginary part of the num4 and round off it to 2 decimal places
'''

# Start of by creating variables
num1,num2,num3=112,20.45,7+3j
sum=num1+num2+num3
print("SUM=",sum)
num4=num2*num3
rem=round(num1%num2,2)
img=round(num4.imag,2)
print("Reminder of "+str(num1)+" and "+str(num2)+" is"+" "+str(rem))
print("Imaginery Part of "+str(num4)+" is"+" "+str(img))
