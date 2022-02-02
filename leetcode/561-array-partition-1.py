from typing import List


class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        print(nums)
        nums.sort()
        print(nums)

        sum = 0
        pair = []
        for num in nums:
            pair.append(num)
            if len(pair) == 2:
                sum += min(pair)
                pair = []
        return sum

solution = Solution()
print(solution.arrayPairSum([1,4,3,2]))