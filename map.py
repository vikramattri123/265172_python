#To update the list
def update(x):
    x=x*2
    return x

nums = [12,21,32,123,34]
s=list(map(update,nums))
print(s)