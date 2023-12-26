class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map, ans = {}, []

        for word in strs:
            chars = tuple(sorted(word))
            if chars in map: ans[map[chars]].append(word)
            else:
                ans.append([word])
                map[chars] = len(ans) - 1

        return ans
