# Rotate array left by k positions

arr = list(map(int, input("Enter elements: ").split()))
k = int(input("Enter rotation value k: "))

n = len(arr)
k = k % n   # handle large k

rotated = arr[k:] + arr[:k]

print("Rotated array:", rotated)
