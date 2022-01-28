from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 풀이 1
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]

        # 풀이 2
        # for i, n in enumerate(nums):
        #     sub_result = target - n
        #     if sub_result in nums[i+1:]:
        #         first = nums.index(n)
        #         second = nums[i+1:].index(sub_result) + i+1
        #         return [first, second]

        # 풀이 3
        nums_map = {}

        for i, num in enumerate(nums):
            nums_map[num] = i
        print(nums_map)

        for i, num in enumerate(nums):
            if target - num in nums_map:
                if i != nums_map[target - num]:
                    return [i, nums_map[target-num]]

solution = Solution()
print(solution.twoSum([2,7,11,15], 9))