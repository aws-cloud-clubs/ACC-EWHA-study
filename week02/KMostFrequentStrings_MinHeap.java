package week02;

import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.PriorityQueue;

public class KMostFrequentStrings_MinHeap {
    static class Pair implements Comparable<Pair> {
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

    public static List<String> kMostFrequentStringsMinHeap(String[] strs, int k) {
        List<String> result = new ArrayList<>();

        Map<String, Integer> freqs = new HashMap<>();
        for (String str : strs)
            freqs.put(str, freqs.getOrDefault(str, 0) + 1);

        PriorityQueue<Pair> minHeap = new PriorityQueue<>();
        for (Map.Entry<String, Integer> entry : freqs.entrySet()) {
            minHeap.add(new Pair(entry.getKey(), entry.getValue()));

            if (minHeap.size() > k)
                minHeap.poll();
        }

        while (!minHeap.isEmpty())
            result.add(minHeap.poll().str);

        Collections.reverse(result);

        return result;
    }
}
