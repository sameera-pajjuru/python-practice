num=int(input("enter the number"))
a=filter(lambda x:(x<num),[1,2,4,5,7,9,12,17,26,45,67,76])
print(list(a))
#ANOTHER MODEL
num=int(input("enter the number"))
a=[1,2,3,4,5,6,7,8,9]
new=[]
for i in a:
    if i<num:
        new.append(i)
print("less than number",list(new))
