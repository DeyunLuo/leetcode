# 给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。 
# 
#  如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。 
# 
#  您可以假设除了数字 0 之外，这两个数都不会以 0 开头。 
# 
#  示例： 
# 
#  输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
# 输出：7 -> 0 -> 8
# 原因：342 + 465 = 807
#  
#  Related Topics 链表 数学 
#  👍 5422 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        result_node = ListNode(0)
        now_node = result_node
        carry = 0
        while l1 or l2:
            x = l1.val if l1 else 0  # 不空就赋值，否则为0
            y = l2.val if l2 else 0
            add_value = x + y + carry
            carry = add_value // 10
            now_node.next = ListNode(add_value % 10)
            now_node = now_node.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            # print(now_node.val)
        if carry:
            now_node.next = ListNode(1)
            # print(now_node.next.val)
        return result_node.next


# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    l1 = ListNode(9)
    l1.next = ListNode(9)
    l1.next.next = ListNode(9)
    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)
    print(Solution().addTwoNumbers(l1, l2))
