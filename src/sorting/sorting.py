# TO-DO: complete the helper function below to merge 2 sorted arrays
# Space complexity: O(len(arrA) + len(aarB))
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    arrA_idx = 0
    arrB_idx = 0
    # loop over the merged_arr
    for idx in range(elements):
        # check if we are at the end of one of the arrays
        # if so, just use other array
        if arrA_idx >= len(arrA):
            merged_arr[idx] = arrB[arrB_idx]
            arrB_idx += 1
        elif arrB_idx >= len(arrB):
            merged_arr[idx] = arrA[arrA_idx]
            arrA_idx += 1


    # compare the first element of each array
     # smaller element goes into merged array
        elif arrA[arrA_idx] < arrB[arrB_idx]:
            merged_arr[idx] = arrA[arrA_idx]
            arrA_idx += 1
        else:
            merged_arr[idx] = arrB[arrB_idx]
            arrB_idx += 1
   



    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here
    if len(arr) <= 1:
        return arr
    else:
        mid = len(arr) // 2
        # recurse on left half
        left = merge_sort(arr[:mid])
        # recurse on right half
        right = merge_sort(arr[mid:])

        # put them back together: merge
        arr = merge(left, right)
    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input


def merge_in_place(arr, start, mid, end):
    # Your code here
    start2 = mid + 1

    if arr[mid] <= arr[start2]:
        return arr

    while start <= mid and start2 <= end:
        # what if start < start2?
        if arr[start] < arr[start2]:
            start += 1
        else:
            # save the second item and its index
            value = arr[start2]
            idx = start2
            # shift everything over one at the time
            while idx != start:
                arr[idx] = arr[idx - 1]
                idx -= 1
            # move the second item over 
            arr[start] = value
            start += 1
            start2 += 1
            mid += 1

            # shift everything over



    pass

# Space complexity: O(1)
def merge_sort_in_place(arr, l, r):
    # Your code here
    if r <= l:
        return arr
    else:
        # find middle
        middle = (r + l) // 2
        # recurse on left and right halves
        merge_sort_in_place(arr, l, middle)
        merge_sort_in_place(arr, middle + 1, r)

        merge_in_place(arr, l, middle, r)
    return arr

