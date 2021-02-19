# bubble sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        is_sorted = True
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                is_sorted = False
        if is_sorted:
            break
    return arr


print(f"bubble sort {bubble_sort([64, 34, 25, 12, 7, 9, 11, 89, 23, 54])}")
