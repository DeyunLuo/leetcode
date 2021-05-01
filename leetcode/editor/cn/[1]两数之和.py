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

class Solution:
    # 第一种暴力破解
    def twoSum(self, nums: [int], target: int) -> [int]:
        position = len(nums) - 1
        for i in range(position):
            for j in range(i + 1, position + 1):
                if nums[i] + nums[j] == target:
                    return i, j

    # 第二种hash table 空间换时间
    def twoSum_1(self, nums: [int], target: int) -> [int]:
        hash_table = {value: key for key, value in enumerate(nums)}
        for key1, value in enumerate(nums):
            diff = target - value
            key2 = hash_table.get(diff)
            if key2 and key1 != key2:
                return key1, key2


if __name__ == '__main__':
    print(Solution().twoSum_1([1, 3, 4, 2], 6))
    # print(Solution().twoSum_1([3, 3], 6))
