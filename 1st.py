def find_two_unique_numbers(arr):
    xor = 0
    
    for num in arr:
        xor ^= num
    
 
    set_bit = xor & -xor
    
    
    num1, num2 = 0, 0
    for num in arr:
        if num & set_bit:
            num1 ^= num  
        else:
            num2 ^= num  
    
   
    return sorted([num1, num2])


arr1 = [1, 2, 3, 2, 1, 4]
print(find_two_unique_numbers(arr1))  

arr2 = [2, 1, 3, 2]
print(find_two_unique_numbers(arr2))  
