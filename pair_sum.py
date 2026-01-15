# Check if pair with given sum exists (two pointers)

arr = list(map(int, input("Enter sorted elements: ").split()))
target = int(input("Enter target sum: "))

left = 0
right = len(arr) - 1
found = False

while left < right:
    current_sum = arr[left] + arr[right]

    if current_sum == target:
        found = True
        break
    elif current_sum < target:
        left += 1
    else:
        right -= 1

if found:
    print("Pair Found")
else:
    print("Pair Not Found")
