/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */

// Time complexity: O(n) where n is the number of nodes in the linked list.
// Space complexity: O(1) as we are reversing the list in-place without using any extra space
class Solution {
    public ListNode reverseList(ListNode head) {
        
        ListNode reversed = null;   
        ListNode current = head;    

        while (current != null) {
            ListNode remaining = current.next; 

            current.next = reversed; 

            reversed = current;       
            current = remaining;     
        }

        return reversed;
    }
}