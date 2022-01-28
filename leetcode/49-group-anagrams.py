import collections
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 애너그램 문자를 키로 사용하고 값은 리스트로 하는 딕셔너리를 만든다
        anagrams = collections.defaultdict(list)
        print(anagrams)

        # strs에 있는 단어들을 순회한다
        for word in strs:
            sorted_word = ''.join(sorted(word))
            # 단어를 정렬한 값을 anagrams의 키로 사용하고
            # 키에 해당하는 리스트에 정렬하지 않은 원래 단어를 append 한다
            anagrams[sorted_word].append(word)
        return list(anagrams.values())


solution = Solution()
print(solution.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
