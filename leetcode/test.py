import collections
import re
from typing import List


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        portfolio = [
            ('GOOG', 100, 490.1),
            ('IBM', 50, 91.1),
            ('CAT', 150, 83.44),
            ('IBM', 100, 45.23),
            ('GOOG', 75, 572.45),
            ('AA', 50, 23.15)
        ]

        total_shares = collections.Counter()
        for name, shares, price in portfolio:
            total_shares[name] += shares
        print(total_shares)

        print(total_shares['GOOG'])
        print(total_shares['IBM'])


solution = Solution()
print(solution.mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"]))