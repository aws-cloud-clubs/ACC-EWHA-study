package week01;

import java.util.Deque;
import java.util.ArrayDeque;
import java.util.HashMap;
import java.util.Map;

public class ValidParenthesisExpression {
    public static boolean validParenthesisExpression(String s) {
        Deque<Character> stack = new ArrayDeque<>();
        Map<Character, Character> parenthesisMap = new HashMap<>();
        parenthesisMap.put('[', ']');
        parenthesisMap.put('{', '}');
        parenthesisMap.put('(', ')');

        for (char c : s.toCharArray()) {
            if (parenthesisMap.containsKey(c))
                stack.push(c);
            else if (c == ']' || c == '}' || c == ')')
                if (!stack.isEmpty() && parenthesisMap.get(stack.peek()) == c)
                    stack.pop();
                else
                    return false;
            else
                return false;
        }

        // 모든 opening parenthesis들이 다 닫혔나 final check
        return stack.isEmpty();
    }
}
