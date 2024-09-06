import numpyexample as np

height = [5.8, 6.2, 5.2, 4.5]
weight = [65.3, 61.2, 35.7, 21.4]

list1 = [round(weight[i] / height[i] ** 2, 3) for i in range(len(weight))]

print(list1)

w = np.array(weight)
h = np.array(height)

#we can directly write mathematical operations when working with similar type of data items
bmi = w / h**2

print(bmi)
