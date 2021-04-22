list =  [2,3,411,33,556,223,55]
s=0
for x in list:
    s=s+x
print(s)

# using while loop some of list element

list = [2,3,411,33,556,223,55]
t=0
s=0
while(t!=len(list)):
       s=s+list[t]
       t=t+1

print(" ",s)