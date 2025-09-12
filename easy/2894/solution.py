class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        nums = set(range(1, n + 1))
        div = set(i for i in nums if i % m == 0)
        return sum(nums - div) - sum(div)


s = Solution()
print(s.differenceOfSums(n=10, m=3))
