class Solution {
    public String solution(String my_string) {

        StringBuilder sb = new StringBuilder(my_string);

        String result = sb.reverse().toString();

        return result;
    }
}