# insert
"""
np.insert(array , index , value , axis=none)
array -> oringinal array
index
value 
axis
axis =0 -> row wise data
axis = 1 -> column wise     
"""

import numpy as np 

arr = np.array([10,20,30,40,50,60,70])
print(arr)
new_arr = np.insert(arr,3,100)
print(new_arr)

# 2d_arr ma kesa ho ga

arr_2d = np.array([[1,2],[3,4]])
print(arr_2d)
new_2d_arr = np.insert(arr_2d , 1 , [5,7],axis=0)
print(new_2d_arr)

# append -> want to add at the last of the array

arr_1 = np.array([20,30,40])
new_arr_1 = np.append(arr_1 , [50,60,70])
print(new_arr_1)

"""
np.concatenate -> ((arr_1 , arr_2 , axis ))
axis 0 -> vertical stacking -> column wise 
axis 1 -> horizontal stacking -> row wise
"""
arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])
new_arr_12 = np.concatenate((arr1 , arr2 ))
print(new_arr_12)


# removing element form the array
"""
np.delete(array , index ,axis=none) //flatten array 
"""

arr_2 = np.array([10,20,30,40,50,60,70])
new_arr_2 = np.delete(arr_2, 3)
print(new_arr_2)

# 2d array 

arra_2d = np.array([[1,2,3],[4,5,6]])
new_2d_arra = np.delete(arra_2d , 0 , axis =1)
print(new_2d_arra)

"""
vstack -> vertically
hstack -> horizontally 

"""
arr01 = np.array([1,2,3])
arr02 = np.array([4,5,6])
print(np.vstack((arr01,arr02)))
print(np.hstack(((arr01,arr02))))