#Exercise 1
tot = int(input("Enter total bill "))
dis=0
if tot >= 1000:
    dis=10
    
total = tot-tot*dis/100
print("Discount:",tot*dis/100)
print("Total Amount:",total)