name=input("enter the name")
backward_name=name[::-1]
if name==backward_name:
    print(name,"is palindrome")
else:
    print(name,"is not palindrome")