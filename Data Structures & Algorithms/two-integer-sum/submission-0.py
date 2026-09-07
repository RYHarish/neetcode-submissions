class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        target_dict = {}
        for index, num in enumerate(nums):
            if target - num in target_dict:
                return [target_dict[target - num], index]
            else:
                if num not in target_dict:
                    target_dict[num] = index