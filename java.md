1st

```java
class Solution {
    public boolean isValid(String s) {
        Stack<Character> leftBrackets = new Stack<>();
        HashMap<Character, Character> brackets = new HashMap<>();
        brackets.put('(', ')');
        brackets.put('{', '}');
        brackets.put('[', ']');
        for (char c : s.toCharArray()) {
            if (brackets.containsKey(c)) {
                leftBrackets.add(c);
                continue;
            }
            if (leftBrackets.isEmpty()) {
                return false;
            }
            if (brackets.get(leftBrackets.peek()) != c) {
                return false;
            }
            leftBrackets.pop();
        }
        return leftBrackets.isEmpty();
    }
}
```

> Stackなのでaddよりはpushが良さそう
