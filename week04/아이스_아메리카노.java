import java.util.stream.IntStream;

class Solution {
    public int[] solution(int money) {
        int[] answer = IntStream.of(
                        money / 5500,
                        money % 5500)
                .toArray();

        return answer;
    }
}