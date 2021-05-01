# 给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。 
# 
#  示例: 
# 
#  输入: [0,1,0,3,12]
# 输出: [1,3,12,0,0] 
# 
#  说明: 
# 
#  
#  必须在原数组上操作，不能拷贝额外的数组。 
#  尽量减少操作次数。 
#  
#  Related Topics 数组 双指针 
#  👍 1048 👎 0

from base import fun_wrapper


# 第一种解法
# 动画演示 https://leetcode-cn.com/problems/move-zeroes/solution/dong-hua-yan-shi-283yi-dong-ling-by-wang_ni_ma/
# 可以理解为将0不断和 后面不为0的元素交换位置
# 快慢指针遍历数组 快慢指针同时开始
# 快指针为正常遍历数组指针
# 当快指针和慢指针数据不相等时 交换快慢指针位置
class Solution:
    @fun_wrapper(input_nums=1)
    def moveZeroes_1(self, nums) -> None:
        num_len = len(nums)
        i = 0
        while i < num_len:
            if nums[i] == 0:
                del nums[i]
                num_len -= 1
            else:
                i += 1
        return nums

    @fun_wrapper(input_nums=1)
    def moveZeroes(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 这种写法比下面一种内存消耗少很多
        # enumerate应该会新开辟内存
        # num_len提前计算好 而不是在range里面计算
        # 2020 5.1第一遍
        slow, nums_len = 0, len(nums)
        for fast in range(nums_len):
            if nums[fast]:
                nums[fast], nums[slow] = nums[slow], nums[fast]
                slow += 1

        # for fast, value in enumerate(nums):
        #     if value != 0:
        #         nums[fast], nums[slow] = nums[slow], nums[fast]
        #         slow += 1
        return nums


if __name__ == '__main__':
    Solution().moveZeroes_1()
