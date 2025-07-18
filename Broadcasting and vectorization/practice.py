import numpy as np 

prices = np.array([100,200,300])
discount = 10

final_price = prices - ( prices*discount/100)

print(final_price)
#  BroadCasting -> expand smaller-> to longer  faster then loop list 

# simple brodacasting
arr = np.array([100,200,300])
result = arr * 3
print(result)

# 2d to 1d array 

matrix = np.array([[1,2,3],[4,5,6]])
vector = np.array([10,20,30])

result = matrix + vector
print (result)

# vectorization -> fast karta ha step ki loop sa bohat fast hota haa 

arr= np.array([10,20,30])
multiplied = arr*4
print(multiplied)