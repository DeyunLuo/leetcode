# 给你单链表的头节点 head ，请你反转链表，并返回反转后的链表。
#  
#  
#  
# 
#  示例 1： 
# 
#  
# 输入：head = [1,2,3,4,5]
# 输出：[5,4,3,2,1]
#  
# 
#  示例 2： 
# 
#  
# 输入：head = [1,2]
# 输出：[2,1]
#  
# 
#  示例 3： 
# 
#  
# 输入：head = []
# 输出：[]
#  
# 
#  
# 
#  提示： 
# 
#  
#  链表中节点的数目范围是 [0, 5000] 
#  -5000 <= Node.val <= 5000 
#  
# 
#  
# 
#  进阶：链表可以选用迭代或递归方式完成反转。你能否用两种方法解决这道题？ 
#  
#  
#  Related Topics 链表 
#  👍 1713 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return
        # next作为占位 pre初始化为链表最后一个节点
        # cur.next pre=cur 即每次都将pre指向前一个节点
        pre, cur = None, head
        while cur:
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next
        return pre
# leetcode submit region end(Prohibit modification and deletion)
