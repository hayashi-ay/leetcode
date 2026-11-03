
1st

```java
class Solution {
    public List<String> generateParenthesis(int n) {
        List<String> allParenthesis = new ArrayList<>();
        buildParenthesis(allParenthesis, new StringBuilder(), n, 0, 0);
        return allParenthesis;
    }

    private void buildParenthesis(List<String> allParenthesis, StringBuilder partial, int n, int numOpen, int numClosed) {
        if (numOpen == n && numClosed == n) {
            allParenthesis.add(partial.toString());
            return;
        }
        if (numOpen < n) {
            partial.append("(");
            buildParenthesis(allParenthesis, partial, n, numOpen + 1, numClosed);
            partial.deleteCharAt(partial.length() - 1);
        }
        if (numClosed < numOpen) {
            partial.append(")");
            buildParenthesis(allParenthesis, partial, n, numOpen, numClosed + 1);
            partial.deleteCharAt(partial.length() - 1);
        }
    }
}
```
