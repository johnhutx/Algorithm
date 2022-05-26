import sys


# Time complexity O(N^2), space complexity O(1)
def selection_sort(arr):
    for i in range(0, len(arr)):    # O(N)
        min_idx = i
        for j in range(i + 1, len(arr)):    # O(N)
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


# Time complexity O(N^2), space complexity O(1)
def bubble_sort_1(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


# Time complexity O(N^2), space complexity O(1)
def bubble_sort_2(arr):
    n = len(arr)
    for i in range(n-1, 0, -1):
        for j in range(0, i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


# Time complexity O(N^2), space complexity O(1)
def insertion_sort_1(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1

        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr


def insertion_sort_2(arr):
    n = len(arr)
    for end in range(1, n):
        newNumIndex = end
        while newNumIndex >= 1 and arr[newNumIndex-1] > arr[newNumIndex]:
            arr[newNumIndex-1], arr[newNumIndex] = arr[newNumIndex], arr[newNumIndex-1]
            newNumIndex -= 1
    return arr


if __name__ == '__main__':
    A = [2, 6, 9, 1, 2, 3, 6, 7, 21, 1, 4]
    A = insertion_sort_2(A)

    print("Sorted array")
    for k in range(len(A)):
        print("%d" % A[k])
