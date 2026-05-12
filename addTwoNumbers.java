class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode temp = new ListNode(0);
        int carryOver = 0;
        ListNode current = temp;
        while (l1 != null || l2 != null || carryOver != 0) {

            int d1 = (l1 == null) ? 0 : l1.val;
            int d2 = (l2 == null) ? 0 : l2.val;
          
            int sum = d1 + d2 + carryOver;
            carryOver = sum / 10;
            current.next = new ListNode(sum % 10);
            current = current.next;
          
            l1 = (l1 != null) ? l1.next : null;
            l2 = (l2 != null) ? l2.next : null;
        }
        return temp.next;
    }
}
