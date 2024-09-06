import numpy as np  
import sys

list1 = list(range(1000))  # Convert range to a list
print("Memory taken by the list=", sys.getsizeof(list1), "Bytes")  # Use getsizeof() directly on the list

arr1 = np.arange(1000)
print("Memory taken by the array=", arr1.nbytes, "Bytes")  # Use nbytes property for NumPy arrays
