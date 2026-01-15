# Check if an array is palindrome using two pointers

arr = list(map(int, input("Enter elements: ").split()))

left = 0
right = len(arr) - 1
is_palindrome = True

while left < right:
    if arr[left] != arr[right]:
        is_palindrome = False
        break
    left += 1
    right -= 1

if is_palindrome:
    print("Palindrome")
else:
    print("Not a Palindrome")
