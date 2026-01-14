# Find duplicate elements in an array

arr = list(map(int, input("Enter elements: ").split()))

freq = {}
duplicates = []

for num in arr:
    freq[num] = freq.get(num, 0) + 1

for key in freq:
    if freq[key] > 1:
        duplicates.append(key)

print("Duplicate elements:", duplicates)
