import numpy as np

arr1 = [280191,114828,156621]
arr2 = [1/32,1/63,1/46]
arr3 = [192,347,311]
arr4 = [11/50,22/50,17/50]
arr5 = [17.3,15.6,13.3]
arr6 = [1/4.33,1/2.45,1/1.3]
arr = [1/18999,1/11999,1/7999]
arr_min = np.min(arr)
arr_std = np.std(arr,ddof=1)
print("最小值为：%f" % arr_min)
print("标准差为:%f" % arr_std)
print((arr-arr_min)/arr_std)
print((arr1-np.min(arr1))/np.std(arr1,ddof=1)+(arr2-np.min(arr2))/np.std(arr2,ddof=1)+(arr3-np.min(arr3))/np.std(arr3,ddof=1)+(arr4-np.min(arr4))/np.std(arr4,ddof=1)+(arr5-np.min(arr5))/np.std(arr5,ddof=1)+(arr6-np.min(arr6))/np.std(arr6,ddof=1)+(arr-arr_min)/arr_std)
