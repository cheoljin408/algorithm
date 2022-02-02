from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # answer = []
        # for i in range(len(nums)):
        #     result = 1
        #     for j in range(len(nums)):
        #         if j != i:
        #             result *= nums[j]
        #     print(result)
        #     answer.append(result)
        #
        # return answer

        answer = []
        result = 1
        for i in range(len(nums)):
            answer.append(result)
            result = result * nums[i]

        result = 1
        for i in range(len(nums)-1, -1, -1):
            answer[i] *= result
            result *= nums[i]

        return answer


solution = Solution()
print(solution.productExceptSelf([1,2,3,4]))
