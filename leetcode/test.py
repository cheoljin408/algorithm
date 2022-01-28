import collections
import re
from typing import List


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = []
        paragraph_split = re.sub(r'[\W]', ' ', paragraph).lower().split()
        for paragraph in paragraph_split:
            if paragraph not in banned:
                words.append(paragraph)

        print(words)
        counts = collections.Counter(words)
        print(counts)
        return counts.most_common(1)[0][0]

solution = Solution()
print(solution.mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"]))