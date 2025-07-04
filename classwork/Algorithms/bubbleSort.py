def bubble_sort(arr):
    """
    Sorts an array using the bubble sort algorithm.
    
    Parameters:
    arr (list): The list of elements to be sorted.
    
    Returns:
    list: The sorted list.
    """
    n = len(arr)
    for i in range(n):
        # Track if a swap was made
        swapped = False
        for j in range(0, n-i-1):
            # Compare adjacent elements
            if arr[j] > arr[j+1]:
                # Swap if they are in the wrong order
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        # If no swaps were made, the array is sorted
        if not swapped:
            break
    return arr

if __name__ == "__main__":
    # Example usage
    sample_array = [64, 34, 25, 12, 22, 11, 90]
    sorted_array = bubble_sort(sample_array)
    print("Sorted array:", sorted_array)