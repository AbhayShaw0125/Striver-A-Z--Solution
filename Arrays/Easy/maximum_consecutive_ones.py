## O(N)
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count=0
        lst=[]
        for i in nums:
            if i==1:
                count=count+1
            else:
                lst.append(count)
                count=0
            lst.append(count)
        return max(lst)
###
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cnt = 0
        maxi = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                cnt += 1
            else:
                cnt = 0
            maxi = max(maxi, cnt)
        return maxi