lst=['Python','C','C++']
if 'Python' not in lst:
    lst.append('Python')
elif 'Java' not in lst:
    lst.append('Java')
else:
    lst.append('JS')
print(lst)

#If Python is not in list then it will print the lst as ['C','C++','Python']
lst1=['C','C++']
if 'Python' not in lst1:
    lst1.append('Python')
elif 'Java' not in lst1:
    lst1.append('Java')
else:
    lst1.append('JS')
print(lst1)

#If both Python, Java is not in list then it will print as ['Python','Java','C','C++','JS']
lst2=['Python','Java','C','C++']
if 'Python' not in lst2:
    lst2.append('Python')
elif 'Java' not in lst2:
    lst2.append('Java')
else:
    lst2.append('JS')
print(lst2)