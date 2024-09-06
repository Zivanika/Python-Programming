dic={
    "Akshat":"Human Being",
    "Spoon":"Object" 
}
print(dic["Akshat"])

employees={
    665:"Harshita",
    646:"Akshat",
    644:"Adrija",
    199:"Akash"
}
# print(employees[655]) #663 raises error cuz not found

print(employees.get(663))  #663 doesn't raise error if not found 

#add new key
employees['degree']='B.Tech'

#removing
employees.pop(644)
# del employees[644]
# del employees
# employees.clear()

new_employeess = employees.copy()



print(employees.values())
print(employees.keys())
# print(employees.items())

for key in employees.keys():
    print(f"The Employee associated with {key} is {employees[key]}")
    
for key, value in employees.items():
  print(f"The value corresponding to the key {key} is {value}") 
  
employees.update({1080:"Suresh"})
print(employees)


