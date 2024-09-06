s1={2,23,5,6,1,2,2,5,}
print(s1)

# Sets are unordered collection of data items. Sets are mutable They store multiple items in a single variable. Set items are separated by commas and enclosed within curly brackets {}. Sets are unchangeable, meaning you cannot change items of the set once created. Sets do not contain duplicate items.

empty_set={}
print(type(empty_set)) #class dict
empty_set=set()
print(type(empty_set)) #class set

s2={100,235,765,666}
# print(s1.union(s2))
# print(s1)
print(s1.update(s2))
print(s1)

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities3 = cities.union(cities2) #you can also use | or operator
print("[Storing in a third variable]")
print(cities3)

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
print("[Updating the first variable]")
cities.update(cities2)
print(cities)

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities3 = cities.intersection(cities2) #you can also use & and operator
print("[Storing in a third variable]")
print(cities3)

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities.intersection_update(cities2)
print("[Updating the first variable]")
print(cities)

#Symmtric Difference = AUB - A∩B. Basically removing the commons.The symmetric_difference() and symmetric_difference_update() methods prints only items that are not similar to both the sets. 

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities3 = cities.symmetric_difference(cities2)
print(cities3)

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities.symmetric_difference_update(cities2)
print(cities)

# The difference() and difference_update() methods prints only items that are only present in the original set and not in both the sets. 

s1={1,2,5,2,7,8,5,3}
s2={2,3,4,6,7}
s3=s1.difference(s2) # - operator can also be used
print(s3)

s1={1,2,5,2,7,8,5,3}
s2={2,3,4,6,7}
s1.difference_update(s2)
print(s3)

# The isdisjoint() method checks if items of given set are present in another set. This method returns False if items are present, else it returns True.
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities3={"Allahabad","New York","London"}
print(cities.isdisjoint(cities2)) 
print(cities.isdisjoint(cities3)) 

# The issuperset() method checks if all the items of a particular set are present in the original set. It returns True if all the items are present, else it returns False.

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Seoul", "Kabul"}
print(cities.issuperset(cities2))
cities3 = { "Madrid"}
print(cities.issuperset(cities3))

# The issubset() method checks if all the items of the original set are present in the particular set. It returns True if all the items are present, else it returns False.

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Delhi", "Madrid"}
print(cities2.issubset(cities))

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.add("Helsinki")
print(cities)

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Helsinki", "Warsaw", "Seoul"}
cities.update(cities2)
print(cities)

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.remove("Tokyo")
print(cities)

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities.remove("Seoul")
cities.discard("Seoul")
print(cities)

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
item = cities.pop()
print(cities)
# This method removes the last item of the set but the catch is that we don’t know which item gets popped as sets are unordered. However, you can access the popped item if you assign the pop() method to a variable.
print(item)


cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
del cities
# print(cities)

# What if we don’t want to delete the entire set, we just want to delete all items within that set?
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.clear()
print(cities)

s4={18,"18"}
print(s4)

s5={20,20.0,"20"}
print(len(s5))

s6={8,7,12,"Harry",[1,2]}
t=list(s6)
t[4]=[2,1]
s6=set(t)
print(s6)


set1 = frozenset([1,2,3,4]) #immutable set
# set1.add(3) # will give error
# print(set1[2]) #doesnt support indexing