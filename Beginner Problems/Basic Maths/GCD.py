class Solution:
    def gcd(self, a, b):
        while a > 0 and b > 0:
            if a > b:
                a = a % b
            else:
                b = b % a
        if a == 0:
            return b
        else:
            return a

obj = Solution()
n1 = int(input("Enter a number: "))
n2 = int(input("Enter a number: "))
gcd = obj.gcd(n1, n2)
print(f"GCD of {n1, n2} is {gcd}")