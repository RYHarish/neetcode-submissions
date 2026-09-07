class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        ans = []
        for s in strs:
            ele = "".join(sorted(s))
            if ele in d:
                d[ele].append(s)
            else:
                d[ele] = []
                d[ele].append(s)

        for e in d:
            ans.append(d[e])

        return ans