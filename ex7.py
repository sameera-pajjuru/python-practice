a= [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
newlist=filter(lambda a: (a%2==0),a)
print("The even numbers are :",list(newlist))