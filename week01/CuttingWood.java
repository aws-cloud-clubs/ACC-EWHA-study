package week01;

import java.util.Arrays;

public class CuttingWood {
    public static int cuttingWood(int[] heights, int k) {
        int bottom, top;
        bottom = 0;
        top = getTallestHeight(heights);

        while (top > bottom) {
            int mid = bottom + (top - bottom) / 2 + 1;  // upper-bound

            if (yieldsEnoughWood(heights, mid, k)) {
                bottom = mid;
            }
            else {
                top = mid - 1;
            }
        }

        return top;
    }

    private static boolean yieldsEnoughWood(int[] heights, int H, int k) {
        int woodCollected = 0;
        for (int height : heights) {
            if (height > H) {
                woodCollected += height - H;
            }
        }

        return woodCollected >= k;
    }

    static int getTallestHeight(int[] heights) {
        if (heights == null || heights.length == 0)
            return 0;

        return Arrays.stream(heights).max().getAsInt();
    }
}
