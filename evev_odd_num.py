# Program to check whether numbers are even or odd

def is_even(n: int) -> bool:
    return n % 2 == 0

def main() -> None:
    s = input("Enter numbers separated by space: ").strip()
    if not s:
        print("No input provided.")
        return
    nums = list(map(int, s.split()))
    for num in nums:
        kind = "even" if is_even(num) else "odd"
        print(f"{num} is {kind}")

if __name__ == "__main__":
    main()