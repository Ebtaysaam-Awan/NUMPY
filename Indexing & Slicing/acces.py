import numpy as np 

arr= np.array([10,20,40,50,60,40,70])
print(arr[0])
print(arr[3])

"""
slicing 

arr[start:stop : step]
arr[start : end] start to end-1
negative step -1 reverse
"""
print(arr[1:5]) #index 1 to 4
print(arr[:4]) #index 0 to 3
print(arr[::3]) # first 3 step
print(arr[::-3])
arr2d = np.array([[1, 2, 3], [4, 5, 6]])
print(arr2d[:, 1])  # Output: [2 5]

# fancy indexing
# always pass as a list
# create copy of selected terms

print(arr[[ 0 , 2 , 4]])
arr2d = np.array([[10, 20], [30, 40], [50, 60]])
print(arr2d[[0, 2], [1, 0]])   # Output: [20 50]


# filtering indexing
# bolean masking
print(arr[arr>25])
print(arr[arr<25])
