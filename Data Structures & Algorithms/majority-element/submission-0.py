class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        length_of_nums = len(nums)

        for n in nums:
            count[n] = 1 + count.get(n, 0)
            if count[n] > length_of_nums / 2:
                return n