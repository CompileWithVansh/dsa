//brute force just for testing tle and practicing 
//time complexity: O(n)
//space complexity: O(n) due to the extra list storing the values of the linked list


class Solution {
    public ListNode reverseList(ListNode head) {
        List<Integer> list = new ArrayList<>();

        ListNode temp = head;

        // Store values
        while (temp != null) {
            list.add(temp.val);
            temp = temp.next;
        }

       
        temp = head;
        int i = list.size() - 1;

        while (temp != null) {
            temp.val = list.get(i--);
            temp = temp.next;
        }

        return head;  
    }
}