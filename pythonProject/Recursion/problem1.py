def findOccurences(arr, key, i):
    if arr[i] == key:
        print(i)
    if i == len(arr) - 1:
        return
    findOccurences(arr, key, i + 1)


findOccurences([3, 2, 4, 5, 6, 2, 7, 2, 2], 2, 0)