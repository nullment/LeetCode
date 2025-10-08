class Solution(object):
    def twoSum(self, nums, target):
        list = []
        i = 0
        for i in range(0, len(nums)):
            j = 0
            for j in range(0, len(nums)):
                if i == j:
                    break
            
                if nums[i] + nums[j] == target:
                    list = [j, i]
        return list\
        
print(Solution().twoSum([2, 7, 11, 15], 9))