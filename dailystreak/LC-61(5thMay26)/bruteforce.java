//At first, I thought of simulating rotation by moving the last node to the front k times, but that would be inefficient (O(k·n)), so we need a better approach
//brute force just for testing tle and practicing
//time complexity: O(k·n) where k is the number of rotations and n is the length of the linked list
//space complexity: O(1) since we are not using any extra space apart from a few pointers

class Solution {
    public ListNode rotateRight(ListNode head, int k) {
        if (head == null || head.next == null) return head;

        int length = getLength(head);
        k = k % length;

        for (int i = 0; i < k; i++) {
            head = rotateOnce(head);
        }

        return head;
    }

    private ListNode rotateOnce(ListNode head) {
        ListNode curr = head;

        // go to second last node
        while (curr.next.next != null) {
            curr = curr.next;
        }

        ListNode last = curr.next;
        curr.next = null;
        last.next = head;

        return last;
    }

    private int getLength(ListNode head) {
        int len = 0;
        while (head != null) {
            len++;
            head = head.next;
        }
        return len;
    }
}