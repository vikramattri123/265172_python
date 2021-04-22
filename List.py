list = ["vikram","Sunil","vikas"]
print(list)

# how to find len of list
list = ["apple","orange","Mango","Pineapple","Grapes"]
print(len(list))

# list type
list = [22,33,44,66,88]
list2 = ["Vikram","Sunil","Vishal"]
list3 = [True,False,True]
print(type(list))
print(type(list2))
print(type(list3))

#append value in list
cars = ["Bmw","audi","Tata","Honda"]
cars.append("Kwid")
print(cars)

#copy one list to another

list = ["one","two","three","four"]
list2 = []
print(list2)
for x in list:
     list2.append(x)
print(list2)