# Program to reverse an array without using built-in reverse

arr = list(map(int, input("Enter elements separated by space: ").split()))

start = 0
end = len(arr) - 1

while start < end:
    arr[start], arr[end] = arr[end], arr[start]
    start += 1
    end -= 1

print("Reversed array:", arr)
