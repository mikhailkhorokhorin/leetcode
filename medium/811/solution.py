from typing import List


class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        nums = {}

        def process(key, val):
            if key not in nums:
                nums[key] = 0
            nums[key] += val

        for i in cpdomains:
            num, domain = int(i.split()[0]), i.split()[1]
            process(domain, num)
            while "." in domain:
                domain = domain.split(".", 1)[1]
                process(domain, num)

        return [f"{v} {k}" for k, v in nums.items()]
