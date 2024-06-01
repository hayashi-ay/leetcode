1st

HashMapのドキュメント。https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/HashMap.html
Integerはintをラップしたクラス。

```java
class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> num_to_index = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            int num_to_find = target - nums[i];
            if (num_to_index.containsKey(num_to_find)) {
                return new int[]{num_to_index.get(num_to_find), i};
            }
            num_to_index.put(nums[i], i);
        }
        return new int[0];
    }
}
```
