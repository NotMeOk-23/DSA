# Brute Force Approach

def countDigits(n):
    cnt = 0
    while n > 0:
        cnt += 1
        n = n // 10
    return cnt

if __name__ == "__main__":
    n = int(input("Enter a number: "))
    print("N:", n)
    digits = countDigits(n)
    print(f"Number of digits: {digits}")

# Optimal Optimal

import math
def countDigits(n):
    cnt = int(math.log10(n) + 1)
    return cnt

if __name__ == "__main__":
    n = int(input("Enter a number: "))
    print(f"N: {n}")
    digits = countDigits(n)
    print(f"Number of digits: {digits}")