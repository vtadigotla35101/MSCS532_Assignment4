def heapify(arr, n, i):
    """
    Maintains the max-heap property for a subtree rooted at index 'i'.
    Assumes that the subtrees are already heapified.

    Args:
        arr: The list (array) representing the heap.
        n: The size of the heap (number of elements in the array to consider).
        i: The index of the root of the subtree to heapify.
    """
    largest = i  # Initialize largest as root
    left_child = 2 * i + 1  # Index of left child
    right_child = 2 * i + 2  # Index of right child

    # If left child exists and is greater than root
    if left_child < n and arr[left_child] > arr[largest]:
        largest = left_child

    # If right child exists and is greater than current largest
    if right_child < n and arr[right_child] > arr[largest]:
        largest = right_child

    # If largest is not root
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Swap
        # Recursively heapify the affected sub-tree
        heapify(arr, n, largest)

def build_max_heap(arr, n):
    """
    Builds a max-heap from an unsorted array.
    This process ensures that the largest element is at the root (index 0).

    Args:
        arr: The list (array) to be converted into a max-heap.
        n: The size of the array.
    """
    # Start from the last non-leaf node and go up to the root
    # The last non-leaf node is at index (n // 2) - 1
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

def heapsort(arr):
    """
    Sorts a list in ascending order using the Heapsort algorithm.

    Steps:
    1. Build a max-heap from the input data.
    2. Repeatedly extract the maximum element from the heap.
       - Swap the root (maximum element) with the last element of the heap.
       - Reduce the size of the heap by 1.
       - Heapify the new root to restore the heap property.

    Args:
        arr: The list to be sorted. It will be sorted in-place.
    """
    n = len(arr)

    # Step 1: Build a max-heap
    # After this step, arr[0] will be the largest element
    build_max_heap(arr, n)

    # Step 2: Extract elements one by one from the heap
    # Loop from the last element down to the first
    for i in range(n - 1, 0, -1):
        # Swap current root (largest element) with the last element of the unsorted part
        arr[i], arr[0] = arr[0], arr[i]

        # Call heapify on the reduced heap (excluding the already sorted last element)
        # to restore the max-heap property for the remaining elements
        heapify(arr, i, 0) # i is the new effective size of the heap


if __name__ == "__main__":
    # Test cases
    data1 = [12, 11, 13, 5, 6, 7]
    print(f"Original array 1: {data1}")
    heapsort(data1)
    print(f"Sorted array 1 (Heapsort): {data1}") # Expected: [5, 6, 7, 11, 12, 13]

    data2 = [4, 10, 3, 5, 1]
    print(f"\nOriginal array 2: {data2}")
    heapsort(data2)
    print(f"Sorted array 2 (Heapsort): {data2}") # Expected: [1, 3, 4, 5, 10]

    data3 = [9, 8, 7, 6, 5, 4, 3, 2, 1] # Reverse sorted
    print(f"\nOriginal array 3 (Reverse Sorted): {data3}")
    heapsort(data3)
    print(f"Sorted array 3 (Heapsort): {data3}") # Expected: [1, 2, 3, 4, 5, 6, 7, 8, 9]

    data4 = [1, 2, 3, 4, 5, 6, 7, 8, 9] # Already sorted
    print(f"\nOriginal array 4 (Already Sorted): {data4}")
    heapsort(data4)
    print(f"Sorted array 4 (Heapsort): {data4}") # Expected: [1, 2, 3, 4, 5, 6, 7, 8, 9]

    data5 = [] # Empty array
    print(f"\nOriginal array 5 (Empty): {data5}")
    heapsort(data5)
    print(f"Sorted array 5 (Heapsort): {data5}") # Expected: []

    data6 = [7] # Single element array
    print(f"\nOriginal array 6 (Single Element): {data6}")
    heapsort(data6)
    print(f"Sorted array 6 (Heapsort): {data6}") # Expected: [7]