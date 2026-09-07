class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        dict_ana = {}
        for i in s:
            if i in dict_ana:
                dict_ana[i] += 1
            else:
                dict_ana[i] = 1

        for j in t:
            if j not in dict_ana:
                return False
            else:
                dict_ana[j] -= 1
                if dict_ana[j] < 0:
                    return False

        return True