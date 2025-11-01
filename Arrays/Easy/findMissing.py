class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        x=len(nums)
        sum1=(x*(x+1)//2)
        sum2=0
        for i in nums:
            sum2+=i
        return sum1-sum2