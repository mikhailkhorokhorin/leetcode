class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        divs = sorted(
            {i for d in range(1, int(n**0.5) + 1) if n % d == 0 for i in (d, n // d)}
        )
        return divs[k - 1] if len(divs) > k else -1
