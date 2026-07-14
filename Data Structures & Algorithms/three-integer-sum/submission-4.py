class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = set()
        for i in range(0, len(nums)):
            myset = set()
            for j in range(i+1, len(nums)):
                third = -(nums[i] + nums[j])
                if third in myset:
                    temp = [nums[i],nums[j],third]
                    temp.sort()
                    result.add(tuple(temp))
                myset.add(nums[j])
        return[list(ans) for ans in result]