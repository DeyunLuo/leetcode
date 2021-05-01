# 给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。 
# 
#  
# 
#  示例 1: 
# 
#  
# 输入: s = "abcabcbb"
# 输出: 3 
# 解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
#  
# 
#  示例 2: 
# 
#  
# 输入: s = "bbbbb"
# 输出: 1
# 解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
#  
# 
#  示例 3: 
# 
#  
# 输入: s = "pwwkew"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
#      请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
#  
# 
#  示例 4: 
# 
#  
# 输入: s = ""
# 输出: 0
#  
# 
#  
# 
#  提示： 
# 
#  
#  0 <= s.length <= 5 * 104 
#  s 由英文字母、数字、符号和空格组成 
#  
#  Related Topics 哈希表 双指针 字符串 Sliding Window 
#  👍 4752 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result_dict = {}
        lst = 0
        for key, value in enumerate(s, start=1):
            result_dict_value = result_dict.get(value)
            if not result_dict_value:
                result_dict[value] = key
                lst += 1
            else:
                if (len(s) - key) > lst:
                    lst = 0
        print(lst)
        return lst


# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    # from collections import defaultdict
    # a = defaultdict(int)
    # print(a.get(10))
    Solution().lengthOfLongestSubstring('abcabcbb')
    # Solution().lengthOfLongestSubstring(' ')
    # Solution().lengthOfLongestSubstring('pwwkew')
    # Solution().lengthOfLongestSubstring('bbbbbbb')
    Solution().lengthOfLongestSubstring('ohomm')
