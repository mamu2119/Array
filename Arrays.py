import array as arr
array_num = arr.array('i', [1, 3, 5, 3, 7, 9, 3])
print("original array:" +str(array_num))
print("NUmber of occurence of the number 3 in the said array:" +str(array_num.count(3)))
array_num.reverse()
print("Reverse the order of the items:")
print(str(array_num))