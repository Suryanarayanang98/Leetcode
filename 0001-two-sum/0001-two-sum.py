class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_dic = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in hash_dic:
                return [hash_dic[diff],i]
            hash_dic[nums[i]] = i