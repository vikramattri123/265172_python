list = ["grapes","orange","apple","Mango"]
v = input("Enter :")
k=0
for i in list:
    # print(i)
    # print(v)
    if i == v:
        k=k+1
if(k>0):
    {
        print("Element Found")
    }
else:
    {
        print("Element Not Found")
    }