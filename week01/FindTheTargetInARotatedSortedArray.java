package week01;

public class FindTheTargetInARotatedSortedArray {
    public static int findTheTargetInARotatedSortedArray(int[] nums, int target) {
        if (nums == null || nums.length == 0) return -1;

        int left, right;
        left = 0;
        right = nums.length - 1;

        while (left < right) {
            int mid = left + (right - left) / 2;

            if (nums[mid] == target)
                return mid;

            // mid를 기준으로 왼쪽/오른쪽 중 한 쪽은 반드시 ascending order일 것
            // Case 1: 왼쪽 => ascending order
            if (nums[left] < nums[mid]) {
                if (nums[left] <= target && target < nums[mid])
                    right = mid - 1;
                else
                    left = mid + 1;
            }
            // Case 2: 오른쪽 => ascending order
            else {
                if (nums[mid] < target && target <= nums[right])
                    left = mid + 1;
                else
                    right = mid - 1;
            }
        }

        return nums[left] == target ? left : -1;
    }
}
