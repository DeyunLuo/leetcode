# 给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。 
# 
#  你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。 
# 
#  
# 
#  示例: 
# 
#  给定 nums = [2, 7, 11, 15], target = 9
# 
# 因为 nums[0] + nums[1] = 2 + 7 = 9
# 所以返回 [0, 1]
#  
#  Related Topics 数组 哈希表 
#  👍 9895 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def twoSum(self, nums: [int], target: int) -> [int]:
        # 最优解 hash_dict
        hash_dict = {}
        for key, value in enumerate(nums):
            another_value = target - value
            if another_value not in hash_dict:
                hash_dict[value] = key
            else:
                return [hash_dict[another_value], key]

    # def twoSum_01(self, nums: [int], target: int) -> [int]:
    #     # 不是最优解
    #     for key, value in enumerate(nums):
    #         another_value = target - value
    #         rest_nums = nums[key + 1:]
    #         if another_value in rest_nums:  # 判断另一个数是否在剩下的列表中
    #             return [key, key + 1 + rest_nums.index(another_value)]


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    print(Solution().twoSum([2, 7, 11, 15], 9))
    # print(Solution().twoSum([3, 3], 6))
