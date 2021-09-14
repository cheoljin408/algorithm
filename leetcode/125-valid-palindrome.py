import collections
import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 풀이1 리스트로 변환
        # s = list(s)
        # only_char = []
        # for i in s:
        #     if i.isalnum():
        #         only_char.append(i.lower())
        #
        # while len(only_char) > 1:
        #     if only_char.pop(0) != only_char.pop():
        #         return False
        #
        # return True
        # ----------------------------
        # 풀이2 데크 자료형 이용 -> 최적화
        # 자료형 데크로 선언
        # strs = collections.deque()
        #
        # for char in s:
        #     if char.isalnum():
        #         strs.append(char.lower())
        #
        # while len(strs) > 1:
        #     if strs.popleft() != strs.pop():
        #         return False
        #
        # return True
        # ----------------------------
        # 풀이3 슬라이싱 사용
        s = s.lower()
        # 정규식으로 불필요한 문자 필터링
        s = re.sub('[^a-z0-9]', '', s)
        return s == s[::-1]


solution = Solution()
print(solution.isPalindrome('A man, a plan, a canal: Panama'))