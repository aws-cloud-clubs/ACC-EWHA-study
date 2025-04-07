package week02;

import java.util.*;

public class EvaluateExpression {
    public static int evaluateExpression(String s) {
        Deque<Integer> stack = new ArrayDeque<>();
        int res = 0;
        int sign = 1;
        int currNum = 0;

        for (char c : s.toCharArray()) {
            if (Character.isDigit(c))
                currNum = currNum * 10 + (c - '0');
            else if (c == '+' || c == '-') {
                res += sign * currNum;

                sign = (c == '+') ? 1 : -1;
                currNum = 0;
            }
            else if (c == '(') {
                stack.push(res);
                stack.push(sign);
                res = 0;
                sign = 1;
            }
            else if (c == ')') {
                res += sign * currNum;

                res *= stack.pop();
                res += stack.pop();

                currNum = 0;
            }
        }

        return res + sign * currNum;
    }
}
