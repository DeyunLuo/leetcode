# 给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有和为 0 且不重
# 复的三元组。 
# 
#  注意：答案中不可以包含重复的三元组。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [-1,0,1,2,-1,-4]
# 输出：[[-1,-1,2],[-1,0,1]]
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = []
# 输出：[]
#  
# 
#  示例 3： 
# 
#  
# 输入：nums = [0]
# 输出：[]
#  
# 
#  
# 
#  提示： 
# 
#  
#  0 <= nums.length <= 3000 
#  -105 <= nums[i] <= 105 
#  
#  Related Topics 数组 双指针
#  👍 3298 👎 0
from typing import List

# 2020 5.1 第一次

class Solution:
    # 1. 暴力求解三层循环
    # 2. hash table 放两数之和
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums_len = len(nums)
        hash_table = {}
        final_result = set()
        for i in range(nums_len - 1):
            for j in range(nums_len):
                hash_table[(nums[i] + nums[j])] = (nums[i], nums[j])

        for key, value in enumerate(nums):
            value2 = hash_table.get(-value)
            if value2:
                result = [value]
                result.extend(value2)
                print(result)
                final_result.update(result)
        return final_result

    def threeSum_1(self, nums: List[int]) -> List[List[int]]:
        # 先排序
        nums.sort()
        final_result = []
        nums_len = len(nums) - 1
        for k in range(nums_len):
            # 判断最小值是否大于0
            if k > 0 and nums[k] == nums[k - 1]:  # 跟上一轮循环的k比较进行 相同就continue 去重
                continue
            left_pointer, right_pointer = k + 1, nums_len  # 初始化左右指针
            while left_pointer < right_pointer:
                sum = nums[left_pointer] + nums[right_pointer] + nums[k]  # 计算三数之和
                if sum == 0:
                    final_result.append([nums[k], nums[right_pointer], nums[left_pointer]])
                    while left_pointer < right_pointer and nums[left_pointer] == nums[left_pointer + 1]:
                        left_pointer += 1
                    while left_pointer < right_pointer and nums[right_pointer] == nums[right_pointer - 1]:
                        right_pointer -= 1
                    left_pointer += 1
                    right_pointer -= 1
                elif sum < 0:
                    left_pointer += 1
                elif sum > 0:
                    right_pointer -= 1
        print(final_result)
        return final_result


if __name__ == '__main__':
    # Solution().threeSum_1([-1, 0, 1, 2, -1, -4])
    Solution().threeSum_1([0, 0, 0])
