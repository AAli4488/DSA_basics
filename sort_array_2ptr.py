# Remove duplicates from sorted array using two pointers

arr = list(map(int, input("Enter sorted elements: ").split()))

if len(arr) == 0:
    print("Empty array")
else:
    slow = 0

    for fast in range(1, len(arr)):
        if arr[fast] != arr[slow]:
            slow += 1
            arr[slow] = arr[fast]

    print("Array after removing duplicates:", arr[:slow+1])
