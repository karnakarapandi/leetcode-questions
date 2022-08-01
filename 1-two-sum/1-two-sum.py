class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num={}
        for i , n in enumerate(nums):
            number = target - n
            if number in num :
                return [i,num[number]]
            num[n]=i