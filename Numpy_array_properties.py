import numpy as np
# arr = np.array([[10,20,30],[40,50,60]])
# print(arr.size)

# # number of dimension

# arr_1d = np.array([1,2,3])
# arr_2d = np.array([[1,2,3],[5,6,7]])
# arr_3d = np.array([[[1,2],[3,4],[5,6],[7,8]]])
# print(arr_1d.ndim)
# print(arr_2d.ndim)
# print(arr_3d.ndim)

# # dtype

# arr_2 = np.array([20,30,40.5])
# print(arr_2.dtype)

# # astype

# arr_3 = np.array([1.1,2.3,4.5])
# int_arr = arr_3.astype(int)
# print(int_arr.dtype)

# # aggregation function
arr = np.array ([20,30,40,])
print(np.sum(arr))
print(np.mean(arr))
print(np.std(arr))
print(np.max(arr))
print(np.min(arr))
print(np.var(arr))
