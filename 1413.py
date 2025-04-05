from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        res = []
        _max = max(candies)

        for i in candies:
            if i + extraCandies >= _max:
                res.append(True)
            else:
                res.append(False)
        return res 