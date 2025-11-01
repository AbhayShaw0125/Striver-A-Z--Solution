##O(Nlog(N))
class Solution:
    def secondLargestElement(self, nums):
        nums.sort()
        maxi = nums[len(nums) - 1]
        secondLargestElement=-1
        for i in nums:
            if i!=maxi:
                secondLargestElement=i
        return secondLargestElement
##O(N)


def secondLargest(self,nums):
    largest=secLarg=float('-inf')
    for num in nums:
        if num > largest:
            secLarg=largest
            largest=num
        elif num >secLarg and num!=largest:
            secLarg=num
    return secLarg