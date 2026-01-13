# Program to find the second largest element in an array

arr = list(map(int, input("Enter elements separated by space: ").split()))

largest = second_largest = -10**18

for num in arr:
    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest and num != largest:
        second_largest = num

if second_largest == -10**18:
    print("Second largest element does not exist")
else:
    print("Second largest element:", second_largest)
