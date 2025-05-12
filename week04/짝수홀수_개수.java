//class Solution {
//    public int[] solution(int[] num_list) {
//        int[] answer = new int[2];
//
//        int evenCount =0;
//        int oddCount=0;
//        for(int i=0; i<num_list.length;i++){
//            if(num_list[i] % 2 ==0){
//                evenCount++;
//            }
//            else
//                oddCount++;
//
//        }
//
//        answer[0]=evenCount;
//        answer[1]=oddCount;
//        return answer;
//    }
//}

import java.util.stream.IntStream;
import java.util.Arrays;

class Solution {
    public int[] solution(int[] numList) {
        int[] answer = {};
        answer = IntStream.of(

                (int)Arrays.stream(numList)
                        .filter(i-> i%2 ==0)
                        .count(),
                (int)Arrays.stream(numList)
                        .filter(i->i%2 ==1)
                        .count()

        ).toArray();
        return answer;
    }
}
