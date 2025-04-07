package week02;

import java.util.ArrayList;
import java.util.Comparator;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.PriorityQueue;

public class KMostFrequentStrings_MaxHeap {
    public static class Pair implements Comparable<Pair> {
        String str;
        int freq;

        public Pair(String str, int freq) {
            this.str = str;
            this.freq = freq;
        }

        @Override
        public int compareTo(Pair other) {
            if (this.freq == other.freq) {
                // reverse lexicographical order
                return other.str.compareTo(this.str);
            }

            // lower-frequency order
            return Integer.compare(this.freq, other.freq);
        }
    }

    public static List<String> kMostFrequentStringsMaxHeap(String[] strs, int k) {
        List<String> result = new ArrayList<>();

        Map<String, Integer> freqs = new HashMap<>();
        for (String str : strs)
            freqs.put(str, freqs.getOrDefault(str, 0) + 1);

        PriorityQueue<Pair> maxHeap = new PriorityQueue<>(Comparator.reverseOrder());

        for (Map.Entry<String, Integer> entry : freqs.entrySet()) {
            maxHeap.add(new Pair(entry.getKey(), entry.getValue()));
        }

        for (int i = 0; i < k && !maxHeap.isEmpty(); i++) {
            result.add(maxHeap.poll().str);
        }

        return result;
    }
}
