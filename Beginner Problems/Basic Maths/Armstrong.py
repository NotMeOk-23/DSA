import math

class Solution:
    def isArmstrong(self, n):
        sum = 0
        number = n
        k = int(math.log10(n) + 1)
        while n > 0:
            digit = n % 10
            n //= 10
            sum += digit ** k
        return sum == number

obj = Solution()
num = int(input("Enter a number: "))
arm = obj.isArmstrong(num)
if arm:
    print("The number is an armstrong number")
else:
    print("The number is not an armstrong number")