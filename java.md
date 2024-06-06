1st

```java
class Solution {
    public int firstUniqChar(String s) {
        HashMap<Character, Integer> charToFreq = new HashMap<>();

        for (char c: s.toCharArray()) {
            int prevFreq = charToFreq.getOrDefault(c, 0);
            charToFreq.put(c, prevFreq + 1);
        }
        for (int i = 0; i < s.length(); i++) {
            if (charToFreq.get(s.charAt(i)) == 1) {
                return i;
            }
        }
        return -1;
    }
}
```
