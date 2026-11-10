class Solution:
    def palindromeCheck(self, n):
        original = n
        rev = 0
        while n > 0:
            digit = n % 10
            rev = rev * 10 + digit
            n //= 10
        return rev == original

obj = Solution()
num = int(input("Enter a number: "))
if obj.palindromeCheck(num):
    print("Palindrome")
else:
    print("Not Palindrome")