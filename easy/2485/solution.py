class Solution:
    def pivotInteger(self, n: int) -> int:
        if n == 1:
            return 1

        arr = list(range(1, n + 1))
        l, r = 0, n - 1
        lsum, rsum = arr[l], arr[r]

        while l < r:
            if lsum < rsum:
                l += 1
                lsum += arr[l]
            elif rsum < lsum:
                r -= 1
                rsum += arr[r]
            else:
                if r - l == 2:
                    return arr[l + 1]
                l += 1
                lsum += arr[l]
                r -= 1
                rsum += arr[r]

        return -1
