# 给你 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, 
# ai) 和 (i, 0) 。找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。 
# 
#  说明：你不能倾斜容器。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  
# 输入：[1,8,6,2,5,4,8,3,7]
# 输出：49 
# 解释：图中垂直线代表输入数组 [1,8,6,2,5,4,8,3,7]。在此情况下，容器能够容纳水（表示为蓝色部分）的最大值为 49。 
# 
#  示例 2： 
# 
#  
# 输入：height = [1,1]
# 输出：1
#  
# 
#  示例 3： 
# 
#  
# 输入：height = [4,3,2,1,4]
# 输出：16
#  
# 
#  示例 4： 
# 
#  
# 输入：height = [1,2,1]
# 输出：2
#  
# 
#  
# 
#  提示： 
# 
#  
#  n = height.length 
#  2 <= n <= 3 * 104 
#  0 <= height[i] <= 3 * 104 
#  
#  Related Topics 数组 双指针 
#  👍 2423 👎 0


from leetcode.editor.cn.base import fun_wrapper


class Solution:
    # 第一种解法 直接暴力枚举 双层循环遍历 计算最大面积
    # 超时
    @fun_wrapper(input_nums=1)
    def maxArea(self, height) -> int:
        con_len = len(height)
        max_area = 0
        for i in range(con_len - 1):
            for j in range(con_len):
                area = min(height[i], height[j]) * (j - i)
                max_area = max(max_area, area)
        return max_area

    # 第二种解法 双指针
    # 木桶原理 木桶最大容量取决于最短那一块
    # 每次移动两个指针对应值的最小值 移动最大值没意义
    # 左右边界同时向中间收敛
    # 2020 5.1第一遍
    @fun_wrapper(input_nums=1)
    def maxArea_1(self, height) -> int:
        i, j = 0, len(height) - 1
        max_area = 0
        while i < j:
            max_area = max(max_area, min(height[j], height[i]) * (j - i))
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return max_area


if __name__ == '__main__':
    Solution().maxArea_1()
