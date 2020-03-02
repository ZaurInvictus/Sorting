# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    # TO-DO

    for i in range(0, elements):
        if len(arrA) < 1:
            merged_arr[i] = arrB[0]
            del arrB[0]
        elif len(arrB) < 1:
            merged_arr[i] = arrA[0]
            del arrA[0]
        elif arrA[0] < arrB[0]:
            merged_arr[i] = arrA[0]
            del arrA[0]
        elif arrB[0] < arrA[0]:
            merged_arr[i] = arrB[0]
            del arrB[0]
    return merged_arr

  # TO-DO: implement the Merge Sort function below USING RECURSION


def merge_sort(arr):
    # TO-DO
    if len(arr) > 1:
        lhs = merge_sort(arr[0: len(arr) // 2])  # // - floor division discards the fractional part 3 // 2 = 1
        rhs = merge_sort(arr[len(arr) // 2:])

        arr = merge(lhs, rhs)
    return arr

# STRETCH: implement an in-place merge sort algorithm


def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr
