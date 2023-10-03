def insertion_sort(arr):
    # Traverse through the entire list starting from the second element.
    for i in range(1, len(arr)):
        # Store the current element to be compared.
        current_element = arr[i]
        # Initialize a variable to keep track of the index to insert the current element.
        j = i - 1

        # Move elements of arr[0..i-1] that are greater than the current element
        # one position ahead of their current position.
        while j >= 0 and current_element < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1

        # Insert the current element at its correct position.
        arr[j + 1] = current_element

# Example usage:
if __name__ == "__main__":
    unsorted_list = [12, 11, 13, 5, 6]
    print("Unsorted list:", unsorted_list)

    insertion_sort(unsorted_list)

    print("Sorted list:", unsorted_list)
