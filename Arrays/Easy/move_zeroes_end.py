class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        lst1 = []
        for i in nums:
            if i != 0:
                lst1.append(i)

        leng = len(nums) - len(lst1)
        lst2 = [0] * leng
        lst3 = lst1 + lst2

        for j in range(len(nums)):
            nums[j] = lst3[j]
