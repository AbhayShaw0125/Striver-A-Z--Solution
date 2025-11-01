class Solution:
    def check(self, nums: List[int]) -> bool:
        mini = min(nums)
        sorted_nums = sorted(nums)

        for i in range(len(nums)):
            if nums[i] == mini:
                lst1 = []
                lst2 = []

                lst1.extend(nums[i:])
                for j in range(0, i):
                    lst2.append(nums[j])

                lst3 = lst1 + lst2

                if lst3 == sorted_nums:
                    return True

        return False
