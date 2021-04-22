list1 = [1,23,455,66,22,442,121,33,55,44]
sum=0
for x in list1:
    sum=sum+x
print("Total Sum of  List:",sum)


# sort element in list
list1 = [32,23,455,66,22,442,121,33,55,44]
v = list1[0]
t=222233
k=0
for x in list1:
    if(x<t):
        t=x
    elif(k<x):
        k=x

print("Smallest No :",t)
print("Largest No: ",k)