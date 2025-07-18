# numpy has builtin function to handle missing values
# np.isnan -> detect missing values
# np.isinf -> to detect infinite values
# Syntax
# np.isnan(array)


arr = np.array([1,2,np.nan,4 ,np.nan])
print(np.isnan(arr))


# 
print(np.nan_to_num(arr))