1st

HashSetのドキュメント。内部的にはHashMapが使われているっぽい。あと順序は保証されない。
https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/HashSet.html

```java
/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public boolean hasCycle(ListNode head) {
        HashSet<ListNode> seen = new HashSet<ListNode>();
        ListNode current = head;
        while (current != null) {
            if (seen.contains(current)) {
                return true;
            }
            seen.add(current);
            current = current.next;
        }
        return false;
    }
}
```

2nd

```java
public class Solution {
    public boolean hasCycle(ListNode head) {
        HashSet<ListNode> seen = new HashSet<>();
        ListNode current = head;
        while (current != null) {
            if (seen.contains(current)) {
                return true;
            }
            seen.add(current);
            current = current.next;
        }
        return false;
    }
}
```
