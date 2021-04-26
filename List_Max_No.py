a = int(input())
list = []
k = 0
for i in range(0, a):
    m = int(input())
    list.append(m)

for i in range(0, a):
    if list[i] > k:
        cl = k
        k = list[i]
        print(k)
        print(cl)
    elif list[i] < k:
        if cl>list[i]:
            cl = list[i]
    elif list[i] == k:
        continue
print(cl)
