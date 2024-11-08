`Arrays.binarySearch`を使った解法。
keyが存在しない場合は`- (insertion point) - 1`が返るようになっていて、マイナス値であることが保証されている。
Pythonの`bisect`モジュールのように素直にinsertion pointを返す実装とどっちが良いかはケースバイケースか。


https://docs.oracle.com/javase/8/docs/api/java/util/Arrays.html#binarySearch-int:A-int-

```java
class Solution {
    public int searchInsert(int[] nums, int target) {
        int ip = Arrays.binarySearch(nums, target);
        if (ip >= 0) {
            return ip;
        }
        return -ip - 1;
    }
}
```
