# 将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：l1 = [1,2,4], l2 = [1,3,4]
# 输出：[1,1,2,3,4,4]
#  
# 
#  示例 2： 
# 
#  
# 输入：l1 = [], l2 = []
# 输出：[]
#  
# 
#  示例 3： 
# 
#  
# 输入：l1 = [], l2 = [0]
# 输出：[0]
#  
# 
#  
# 
#  提示： 
# 
#  
#  两个链表的节点数目范围是 [0, 50] 
#  -100 <= Node.val <= 100 
#  l1 和 l2 均按 非递减顺序 排列 
#  
#  Related Topics 递归 链表 
#  👍 1683 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# Definition for singly-linked list.
import sys
import io
import json


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dumb_node = ListNode(0)
        res = dumb_node
        while l1 and l2:
            if l1.val < l2.val:
                res.next, l1 = l1, l1.next
            else:
                res.next, l2 = l2, l2.next
            res = res.next
            if l1:
                res = l1.next
            if l2:
                res = l2.next
        return dumb_node.next


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


def readlines():
    for _ in range(2):
        yield input('please input list')
    # for line in io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8'):
    #     print(line.strip('\n'))
    #     yield line.strip('\n')


def main():
    lines = readlines()
    while True:
        try:
            line = next(lines)
            l1 = stringToListNode(line)
            line = next(lines)
            l2 = stringToListNode(line)

            ret = Solution().mergeTwoLists(l1, l2)

            out = listNodeToString(ret)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
