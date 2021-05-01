# 请判断一个链表是否为回文链表。 
# 
#  示例 1: 
# 
#  输入: 1->2
# 输出: false 
# 
#  示例 2: 
# 
#  输入: 1->2->2->1
# 输出: true
#  
# 
#  进阶： 
# 你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？ 
#  Related Topics 链表 双指针 
#  👍 959 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 1. 快慢指针同时开始 快指针一步 慢指针两步 先拿出前半部分链表和后半部分链表
# 2. 后半部分链表反转
# 3. 比较链表
class Solution:
    def find_pre_back_node(self, head):
        # 快慢指针分割链表 最后慢指针为前部分列表的最后一个node
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow.next  # 返回后半部分链表的头结点

    def reverse_node(self, head):
        pre, cur = None, head
        while cur:
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next
        return pre

    def isPalindrome(self, head: ListNode) -> bool:
        if not head or not head.next or not head.next.next:
            return False
        back_node = self.find_pre_back_node(head)
        reverse_node = self.reverse_node(back_node)
        while head and reverse_node:  # 此处只能判断全链表和后半部分反转链表 因为中间值
            if head.val != reverse_node.val:
                return False
            head, reverse_node = head.next, reverse_node.next
        return True

# leetcode submit region end(Prohibit modification and deletion)
