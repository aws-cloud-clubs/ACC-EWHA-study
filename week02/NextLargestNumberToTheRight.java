package week02;

import java.util.Deque;
import java.util.ArrayDeque;

public class NextLargestNumberToTheRight {
    public static int[] nextLargestNumberToTheRight(int[] nums) {
        int[] res = new int[nums.length];
        Deque<Integer> candidates = new ArrayDeque<>();

        // 왼쪽이 아닌 '오른쪽'부터 탐색
        for (int i = nums.length - 1; i >= 0; i--) {
            // 1. 현재 막대의 추가로 인해 자격을 잃게 되는 candidate들 제거하기
            while (!candidates.isEmpty() && nums[i] >= candidates.peek())
                candidates.pop();

            // 2. 현재 막대의 next largest number to the right 기록하기
            res[i] = candidates.isEmpty() ? -1 : candidates.peek();

            // 3. 현재 막대를 새로운 candidate로 추가하기
            candidates.push(nums[i]);
        }

        return res;
    }
}

