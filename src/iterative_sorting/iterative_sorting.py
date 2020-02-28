# We start at the first index and loop through every index. Within that loop we loop through every item to the right of our current index and find the smallest value. Once we have smallest value, we compare to our original value and if smallest value is smaller than original then we swap them.

# TO-DO: Complete the selection_sort() function below 
    # loop through n-1 elements
      # current index is the one we check / compare to.
        # smallest index should equal the index of the smallest value once we loop through every value to the right of our current index
        # TO-DO: find next smallest element
        # loop through all values to the right of where our current index is
          # if the index of this iteration is smaller than the smallest index
            # smallest index = that index
        # TO-DO: swap
        # compare our current index to smallest index
          # if smallest index is smaller than current index
            # swap them
def selection_sort( arr ):
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[smallest_index]:
               smallest_index = j

        if smallest_index != i:
          swapped = arr[i]
          arr[i] = arr[smallest_index]
          arr[smallest_index] = swapped
    return arr


# Loop through the entire array and compare the current value to the value to the right of it. If the current value is larger than the one to the right, swap them. Keep doing this until a swap does not happen.

# TO-DO:  implement the Bubble Sort function below
  # while swap happened
    # loop through the array and compare values
      # if value at current index is bigger than value at index to the right.
        # swap them
        # The largest value should end up at the end
        # once that value is at the end then you just start the while over 
        # keep doing this until a swap doesn't happen
def bubble_sort(arr):
    for i in range(0, len(arr) - 1):
        cur_index = i
        swapped = False
        for j in range(i + 1, len(arr)):
            next_index = j
            x = arr[cur_index]
            y = arr[next_index]
            if arr[i] > arr[j]:
                arr[cur_index] = y
                arr[next_index] = x
                swapped = True
        if swapped == False:
            break

    return arr





# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):
    return arr