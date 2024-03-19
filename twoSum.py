from typing import List
from decoratorFunction import decorator_function

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 1
        # hashmap = {}
        # for i in range(len(nums)):
        #     hashmap[nums[i]] = i
        # for i in range(len(nums)):
        #     complement = target - nums[i]
        #     if complement in hashmap and hashmap[complement] != i:
        #         return [i, hashmap[complement]]

        # 2
        hashmap = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap:
                return [i, hashmap[complement]]
            hashmap[nums[i]] = i
        
        # 3
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return([i, j])

                
if __name__ == '__main__':
    ITER = 1000
    sol = Solution
    nums: List[int] = [2,7,11,15,20,35, 33, 21, 100, 55, 76, 51, 2700, 4500, 28000, 456, 982, 1000, 50]
    target: int = 1050

    run_function = decorator_function(sol.twoSum)

    average_value = 0
    for i in range(ITER):
        average_value += float(run_function(sol, nums, target))
    average_value/=ITER
    print(average_value)