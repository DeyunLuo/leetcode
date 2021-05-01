# 存在一个按升序排列的链表，给你这个链表的头节点 head ，请你删除所有重复的元素，使每个元素 只出现一次 。 
# 
#  返回同样按升序排列的结果链表。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：head = [1,1,2]
# 输出：[1,2]
#  
# 
#  示例 2： 
# 
#  
# 输入：head = [1,1,2,3,3]
# 输出：[1,2,3]
#  
# 
#  
# 
#  提示： 
# 
#  
#  链表中节点数目在范围 [0, 300] 内 
#  -100 <= Node.val <= 100 
#  题目数据保证链表已经按升序排列 
#  
#  Related Topics 链表 
#  👍 567 👎 0

import json

# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# class Solution:
#     def deleteDuplicates(self, head: ListNode) -> ListNode:
#         while True:
#             if not head.next:
#                 break
#             elif head.next.val == head.val:
#                 head.next = head.next.next
#         return head
# leetcode submit region end(Prohibit modification and deletion)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return head
        pre, cur = head, head.next
        while cur:
            if pre.val == cur.val:
                pre.next = cur.next
            else:
                pre = cur
            cur = cur.next
        return head


def stringToIntegerList(input):
    return json.loads(input)


def stringToListNode(input):
    # Generate list from the input
    numbers = stringToIntegerList(input)

    # Now convert that list into linked list
    dummyRoot = ListNode(0)
    ptr = dummyRoot
    for number in numbers:
        ptr.next = ListNode(number)
        ptr = ptr.next

    ptr = dummyRoot.next
    return ptr


def listNodeToString(node):
    if not node:
        return "[]"

    result = ""
    while node:
        result += str(node.val) + ", "
        node = node.next
    return "[" + result[:-2] + "]"


def main():
    import sys
    import io
    def readlines():
        yield input('please input list')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            head = stringToListNode(line);

            ret = Solution().deleteDuplicates(head)

            out = listNodeToString(ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
