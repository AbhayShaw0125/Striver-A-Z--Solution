class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        temp = sorted(set(nums))
        for i in range(len(temp)):
            nums[i] = temp[i]
        return len(temp)
