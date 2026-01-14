# Find missing number from 1 to N

arr = list(map(int, input("Enter elements: ").split()))
n = len(arr) + 1

total_sum = n * (n + 1) // 2
array_sum = sum(arr)

missing = total_sum - array_sum

print("Missing number:", missing)
