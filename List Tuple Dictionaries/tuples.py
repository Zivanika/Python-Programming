tup=(1,2)
print(type(tup),tup) #Gives class tuple
tup=(1)
print(type(tup),tup) #Gives class int so always tup=(1,) give comma

# Tuples are immutable, hence if you want to add, remove or change tuple items, then first you must convert the tuple to a list. Then perform operation on that list and convert it back to tuple.

cars=("Lamborghini","BMW","Audi","Porsche")
# cars[2]="Buggati"
temp = list(cars)  #Converting tuple to list
temp.pop(2)  #Popping 2nd element
temp.append("Ferrari") 
cars=tuple(temp) #Converting back to tuple
print(cars)

countries = ("Pakistan", "Afghanistan", "Bangladesh", "ShriLanka")
countries2 = ("Vietnam", "India", "China")
southEastAsia = countries + countries2  #Can add 2 tuples to create a 3rd one
print(southEastAsia)

tuple1 = (0, 1, 2, 3, 2, 31, 1, 3, 2, 3)
res = tuple1.count(3)  #counts three's occurences in the tuple
# res = tuple1.index(3) #first occurence
# res = tuple1.index(3, 4, 8) #first occurence b/t 4-8 index
# res = len(tuple1)
print('Count of 3 in tuple1 is:', res)