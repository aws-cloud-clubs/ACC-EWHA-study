package week03;

import datatype.ListNode;

import java.util.Comparator;
import java.util.List;
import java.util.PriorityQueue;

public class CombineSortedLinkedList {
    public static ListNode combineSortedLinkedLists(List<ListNode> lists) {
        PriorityQueue<ListNode> minHeap = new PriorityQueue<>(Comparator.comparingInt(self -> self.val));
        for (ListNode head : lists)
            if (head != null) minHeap.offer(head);

        ListNode dummy = new ListNode(-1);
        ListNode currNode = dummy;
        while (!minHeap.isEmpty()) {
            ListNode smallestNode = minHeap.poll();
            currNode.next = smallestNode;
            currNode = currNode.next;
            if (smallestNode.next != null)
                minHeap.offer(smallestNode.next);
        }

        return dummy.next;
    }
}
