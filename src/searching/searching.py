#TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # Your code here
   
    if len(arr) <= 0:
        return -1

    middle = (start + end) // 2
    if arr[middle] == target:
        return middle
    else:
        if target < arr[middle]:
            end = middle + 1            
        
        else:
            start = middle - 1
    
    return binary_search(arr, target, start, end)
    
    
    
### Implement an iterative implementation of binary search

# def binary_search(arr, target):
   
#     # keep track of upper and lower bounds
#     low = 0
#     high = len(arr) - 1

#     while low < high:
#     # find the middle of those bounds
#         middle = (low + high) // 2
        
#         # check if this is our target
#         if target == arr[middle]:
#             return middle

#         # check if target is above or below the middle
#         # move upper or lower bound to the middle( to cut array in half)

#         elif target > arr[middle]:
#             low = middle - 1
#         elif target < arr[middle]:
#             high = middle + 1
#     return -1

    


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
    # Your code here
    pass

