//class Solution {
//    public int[] solution(int[] num_list) {
//        int[] answer = new int[num_list.length];
//        for (int i = 0; i < num_list.length; i++) {
//            answer[i] = num_list[num_list.length - 1 - i];
//        }
//        return answer;
//    }
//}

import java.util.*;
import java.util.stream.*;

class Solution {
    public int[] solution(int[] num_list) {

        List<Integer> list = Arrays.stream(num_list) // num_list 은 기본형 배열이므로, 이를 스트림 연산을 하면 IntStream이 된다.
                .boxed() // int -> Integer
                .collect(Collectors.toList());

        Collections.reverse(list);

        int[] answer = list.stream()
                .mapToInt(Integer::intValue) // Integer -> int
                .toArray();

        return answer;
    }
}
