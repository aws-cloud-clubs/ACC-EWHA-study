package week03;

import java.util.Comparator;
import java.util.PriorityQueue;

public class MedianOfAnIntegerStream {

    PriorityQueue<Integer> leftHalf;     // Max Heap
    PriorityQueue<Integer> rightHalf;    // Min Heap

    public MedianOfAnIntegerStream() {
        leftHalf = new PriorityQueue<>(Comparator.reverseOrder());
        rightHalf = new PriorityQueue<>();
    }

    public void add(int num) {
        if (leftHalf.isEmpty() || num <= leftHalf.peek()) {
            leftHalf.offer(num);

            if (leftHalf.size() > rightHalf.size() + 1)
                rightHalf.offer(leftHalf.poll());
        }
        else {
            rightHalf.offer(num);

            if (leftHalf.size() < rightHalf.size())
                leftHalf.offer(rightHalf.poll());
        }
    }

    public float getMedian() {
        if (leftHalf.isEmpty()) return 0;

        if (leftHalf.size() == rightHalf.size())
            return (leftHalf.peek() + rightHalf.peek()) / 2f;

        return leftHalf.peek();
    }
}
