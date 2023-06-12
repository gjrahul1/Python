#Exercise 2
#QUESTION: Get the input from the user and check if the customer brought purchased the product.
a=int(input("Enter the price of the product"))
b=input("Did the customer purchase the product ?")
dis=0
#'Yes' - True #'No' - False
if (b=='Yes'or b=='yes') or (b=='No'or b=='no'):
    if (b=='Yes'or b=='yes'):
        cond=True
        print("Customer purchased the product")
        if a<1000:
            print("Customer cannot avail the discount")
            total = a-a*dis/100
            print("Amount to be paid ",total)
    elif (b=='No' or b=='no'):
        cond=False
        print("Customer didn't purchase the product")
    if a>=1000 and cond:
        dis=10
        total = a-a*dis/100
        print("Discount ",dis)
        print("Amount to be paid ",total)
else:
 print("Please purchase to bill the product ")