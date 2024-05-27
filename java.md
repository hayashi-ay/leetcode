1st

```java
/**
 * Definition for singly-linked list.
 * public class ListNode {
 * int val;
 * ListNode next;
 * ListNode() {}
 * ListNode(int val) { this.val = val; }
 * ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    private int getValue(ListNode node) {
        if (node == null) {
            return 0;
        }
        return node.val;
    }

    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {

        ListNode sentinel = new ListNode();
        ListNode prev = sentinel;
        int carry = 0;
        while (l1 != null || l2 != null || carry != 0) {
            int sum = getValue(l1) + getValue(l2) + carry;
            carry = sum / 10;
            ListNode node = new ListNode(sum % 10);
            prev.next = node;
            prev = prev.next;
            if (l1 != null) {
                l1 = l1.next;
            }
            if (l2 != null) {
                l2 = l2.next;
            }
        }
        return sentinel.next;
    }
}
```
