import java.util.Arrays;

class Solution {
    public double solution(int[] numbers) {
        double answer = 0;
        answer = Arrays.stream(numbers).average().orElse(0);
        return answer;
    }
}

/*

class Solution {
    public double solution(int[] numbers) {
        double answer = 0;

        // 배열의 길이는 속성이므로 괄호 없다.
        // 문자열의 경우 length()는 메서드.
        int total =0;
        for(int i=0; i<numbers.length;i++){

            total += numbers[i];
        }
        // double로 변환해서 실수 계산하도록.
        answer = total/ (double)numbers.length;
        return answer;
    }
}
 */