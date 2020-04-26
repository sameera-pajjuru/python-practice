num=int(input("enter the number "))
list1=[2,4,3,5,7,8,25,14,52,4]
new_list=list(map(lambda x:x/num,list1))
print(tuple(new_list))