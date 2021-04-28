# Program to Check Even No in List
def even(x):
    if(x%2==0):
        return x


a = int(input("Enter no : "))
list1 = []
for i in range(0,a):
    v=int(input("Enter No to Add : "))
    list1.append(v)
print(list1)
s =list(filter(even,list1))
print("Even No in the List are ",s)