class Solution:
    def convert(self, number: int, to_base: int) -> str:
        digits = []
        while number > 0:
            remainder = number % to_base
            if remainder < 10:
                digits.append(str(remainder))
            else:
                digits.append(chr(ord("A") + remainder - 10))
            number //= to_base

        return "".join(reversed(digits))

    def isPalindromic(self, number: str):
        print(number)
        return number == number[::-1]

    def isStrictlyPalindromic(self, n: int) -> bool:
        # return False
        return all([self.isPalindromic(self.convert(n, base)) for base in range(2, n - 1)])


s = Solution()
print(s.isStrictlyPalindromic(4))
