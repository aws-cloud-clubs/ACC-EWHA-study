import java.util.*;
import java.util.stream.*;

class Solution {
    public int[] solution(int n) {
        int[] answer = {};

        List<Integer> list = new ArrayList<>();

        for(int i=0; i<n;i++){

            if(n % (i+1) ==0 ){
                list.add(i+1);
            }
        }
        answer = list.stream()
                // i->i 도 가능. 자동 언박싱
                .mapToInt(Integer::intValue)
                .toArray();

        return answer;
    }
}