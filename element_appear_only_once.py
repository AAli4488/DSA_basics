# Find elements that appear only once

arr = list(map(int, input("Enter elements: ").split()))

freq = {}

for num in arr:
    freq[num] = freq.get(num, 0) + 1

print("Unique elements:")
for key in freq:
    if freq[key] == 1:
        print(key, end=" ")
