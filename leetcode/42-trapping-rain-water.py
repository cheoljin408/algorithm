from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        # 풀이 1
        # if not height:
        #     return 0
        #
        # volume = 0
        # left, right = 0, len(height)-1
        # left_max, right_max = height[left], height[right]
        #
        # while left < right:
        #     left_max, right_max = max(height[left], left_max), max(height[right], right_max)
        #
        #     if left_max <= right_max:
        #         volume += left_max - height[left]
        #         left += 1
        #     else:
        #         volume += right_max - height[right]
        #         right -= 1
        #
        # return volume

        # 풀이 2
        stack = []
        volume = 0

        for i in range(len(height)):
            while stack and height[i] > height[stack[-1]]:
                top = stack.pop()

                if not len(stack):
                    break

                distance = i -stack[-1] - 1
                waters = min(height[i], height[stack[-1]]) - height[top]

                volume += distance * waters

            stack.append(i)
        return volume


solution = Solution()
print(solution.trap([0,1,0,2,1,0,1,3,2,1,2,1]))
