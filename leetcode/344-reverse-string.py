from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        # 풀이1 파이썬다운 방식
        s.reverse()

        # 풀이2 투 포인터를이용한 스왑
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
