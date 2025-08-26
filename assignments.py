import numpy as np

"""
Create a NumPy array of shape (5, 5) filled with random integers between
1 and 20. Replace all the elements in the third column with 1.
"""

# arr1 = np.array([1,2,3,5,6,5,56,63,11,13,34,56,565,656,4,546,53,211,6,123,656,1,356,6,1331])
# print(arr1.shape)

# re_arr1 = np.reshape(arr1,(5,5))
# re_arr1[:,2]=1

# print(re_arr1)
"""
Create a NumPy array of shape (4, 4) with values from
1 to 16. Replace the diagonal elements with 0.
"""
# arr2 = np.arange(1,17).reshape(4,4)
# print(arr2)
# np.fill_diagonal(arr2,0)
# print(arr2)

"""
Creat Numpy array of shape(6,6) withvalues from 1 to 36.
Extract the sub-array consisting of the 3rd to 5th rows and 2nd to
4th columns
"""
# arr3 = np.arange(1,37).reshape(6,6)
# print(arr3)
# print(arr3[2:5,1:4])

"""
Create a Numpy array of shape(5,5) Extract the elements on the border
"""
# arr4 = np.random.randint(1,25,size=(5,5))
# print(arr4)
# border_arr = np.concatenate((arr4[0,:],arr4[-1,:],arr4[1:-1,0],arr4[1:-1,-1]))
# print("Border Elements:",border_arr)

"""
Create 3x4 with random integer perform element wise add,sub, mult,div
"""
# arr5 = np.random.randint(1,58,size=(3,4))
# arr6 = np.random.randint(1,58,size=(3,4))
# arr_sum = np.add(arr5,arr6)
# arr_diff = np.subtract(arr5,arr6)
# arr_mult = np.multiply(arr5,arr6)
# arr_div = np.divide(arr5,arr6)
# print("Sum:",arr_sum)
# print("Sub:", arr_diff)
# print("Product:",arr_mult)
# print("Division:",arr_div)

"""
Create 4x4 array and perform column wise and row wise sum
"""
arr7 =  np.arange(1,17).reshape(4,4)
print(arr7)
row_sum = np.sum(arr7,axis=1)
column_sum =  np.sum(arr7,axis=0)

print("Row wise sum:",row_sum)
print("Column wise sum:",column_sum)
