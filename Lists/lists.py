#Homogenous List Example

a=[1,2,3,4]
b=[1.0,1.2,1.3,1.4]
c=['A','B','C','D']
print("Number List:",a)
print("Float List:",b)
print("String list:",c)

#Heterogenous List Example

a=[1,1.4,'Python']
print("Heterogenous List:",a)

#Slicing & Updation of a List

lst=['Python','C','C++']
print("Before Update:",lst)
lst[-1]='Java'
print("After Update:",lst)
print("",lst[2:]) #Slicing the list, print the list after 2nd element

#Merging & Unpacking List

lst1=[0,2,4,6] #List of even numbers incl 0
print('Even List:',lst1)
lst2=[1,3,5,7] #List of odd numbers
print("Odd List:",lst2)
temp=[lst1,lst2] #Merged as single list
print("Merged List:",temp)
temp=[lst1+lst2] #can only merge the list using '+' operator can't use other arthmetic operators
print("Single Merged List:",temp)
temp=[*lst1,*lst2]
print("Single List:",temp)

#Built-In Functions

print("We are learning list using built-in functions")
print("Original List:",temp)
# temp.append(i) - we can't directly send the parameter as it is string 
temp.append(7) 
print("New List:",temp)
print("Sorting the list")
temp.sort()
    #print("",temp.sort()) - will give the output as None Datatype
    
print("",temp) #sorting doesn't take place for heterogenous elements
print("Reversing the list")
temp.reverse()
    #print("",temp.reverse()) - will give the output as None Datatype
    
print("",temp)
temp.remove(5) #alternatively we can use pop() function to delete element which uses indexing
del(temp[3]) #deleting 3rd index 
print("Modified List:",temp)
count=temp.count(7)
print("The list contains "+str(count)+" elements ")
i=temp.index(1) #index() gives us the index value of an element in the list
print("Index of 1 is %d"%i)

#clearning the list
temp.clear()
print("List is now empty")
print("",temp)
#adding an element to the list

#temp=temp+temp[0] - throws IndexError [cannot add values to the index]
temp=temp+[0]+[6]+[1]
print("",temp)

#Using membership operators
print(bool(6 in temp))
print(bool(5 in temp))

#print(6 in temp) - can print the same output without boolean function since membership operators are boolean in naturer