
//Convert list to circular, move to (n - k)th node, break to get rotated list
//time complexity: O(n) where n is the length of the linked list
//space complexity: O(1) since we are not using any extra space apart from a few pointers
/*
Step 1: tail.next = head;

Before:
1 → 2 → 3 → 4 → 5 → null
After:
1 → 2 → 3 → 4 → 5
↑                   ↓
← ← ← ← ← ← ← ← ← ←
Step 2: Move tail to (n - k)th node */

class Solution {
    public ListNode rotateRight(ListNode head, int k) {
        if (head == null || head.next == null) return head;

        ListNode tail = head;
        int n = 1;

        while (tail.next != null) {
            tail = tail.next;
            n++;
        }

        k %= n;
        if (k == 0) return head;

        tail.next = head; 

        for (int i = 0; i < n - k; i++) {
            tail = tail.next;
        }

        ListNode newHead = tail.next;
        tail.next = null;

        return newHead;
    }
}
