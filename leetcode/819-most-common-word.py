from typing import List
import re

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        s = paragraph.lower()
        s = re.sub('[^a-z ]', ' ', s)
        list_s = s.split()
        print(list_s)
        dict_s = dict()
        for ele in set(list_s):
            dict_s[ele] = 0

        for i in list_s:
            if i not in banned and i in dict_s:
                dict_s[i] += 1

        print(dict_s)

        dict_max = max(dict_s, key=dict_s.get)
        print(dict_max)

        return dict_max


solution = Solution()
print(solution.mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"]))