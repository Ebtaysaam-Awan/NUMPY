# Resahping is the process where you change the dimension of array without modifying the array data
# like 1d array to 2d array
# total number of element remain the same in the array after conversion
"""
reshape(rows , columns) specify new shape if dimension match
"""
import numpy as np 

arr = np.array([10,20,30,40,50,60])
reshaped_arr = arr.reshape(2,3)
print(reshaped_arr)
# reshape only change the view not array

"""
.raval() -> view return kara ga
.flatten() -> copy return kara ga
"""

arr_2d = np.array([[1,2,3],[4,5,6]])
print(arr_2d.ravel())
print(arr_2d.flatten())
# concatenate
a = np.array([[1, 2]])
b = np.array([[3, 4]])
print(np.concatenate((a, b), axis=0)) #axis 0 par row column or axis 1 par only 1d array

# spilt kar aga tora ga 
a = np.array([1, 2, 3, 4, 5, 6])
print(np.split(a, 3))  # Output: [array([1,2]), array([3,4]), array([5,6])]

# squeeze one length dimension remove karta ha 
a = np.array([[[1], [2], [3]]])
print(np.squeeze(a))  # Output: [1 2 3]


