import java.util.HashSet;
import java.util.Set;

class Solution {
    public int solution(int N, int number) {
        List<Set<Integer>> dp = new ArrayList<>();

        for (int i = 0; i < 9; i++) {
            dp.add(new HashSet<>());
        }

        for (int i = 1; i < 9; i++) {
            int num = 0;
            // 이어 붙이기 5, 55, 555
            for (int k = 0; k < i; k++) {
                num = num * 10 + N;
            }
            dp.get(i).add(num);

            for (int j = 1; j < i; j++) {
                Set<Integer> temp = new HashSet<>();
                for (int a : dp.get(j)) {
                    for (int b : dp.get(i - j)) {
                        temp.add(a + b);
                        temp.add(a - b);
                        temp.add(a * b);
                        if (b != 0) temp.add(a / b);
                    }
                }
                dp.get(i).addAll(temp); // 한 번에 추가해서 예외 방지
            }

            if (dp.get(i).contains(number)) return i;
        }

        return -1;
    }
}
