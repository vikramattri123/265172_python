# print only even no from range of Numbers
a = int(input())
for x in range(1,a):
    if x%2==1:
        continue
    else:
        print(x)

# find No in the list
Nums = [22,1,22,55,66,777,34,90]
b = int(input())
for x in Nums:
    if x==b:
        print("Found")
        break
    else:
        continue

