# Program to find the largest element in an array

arr = list(map(int, input("Enter elements separated by space: ").split()))

largest = arr[0]

for num in arr:
    if num > largest:
        largest = num

print("Largest element:", largest)
