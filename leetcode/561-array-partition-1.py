from typing import List


class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        # 풀이 1
        # print(nums)
        # nums.sort()
        # print(nums)
        #
        # sum = 0
        # pair = []
        # for num in nums:
        #     pair.append(num)
        #     if len(pair) == 2:
        #         sum += min(pair)
        #         pair = []
        # return sum

        # 풀이 2
        return sum(sorted(nums)[::2])

solution = Solution()
print(solution.arrayPairSum([1,4,3,2]))