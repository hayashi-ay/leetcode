1st

PriorityQueue
```java
class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        HashMap<Integer, Integer> numToFreq = new HashMap<>();
        PriorityQueue<Integer> topKFrequentHeap = new PriorityQueue<>(
            (n1, n2) -> numToFreq.get(n1) - numToFreq.get(n2)
        );
        for (int num : nums) {
            numToFreq.put(num, numToFreq.getOrDefault(num, 0) + 1);
        }
        for (int num: numToFreq.keySet()) {
            topKFrequentHeap.add(num);
            if (topKFrequentHeap.size() > k) {
                topKFrequentHeap.poll();
            }
        }

        int[] topK = new int[k];
        for (int i = 0; i < k; i++) {
            topK[i] = topKFrequentHeap.poll();
        }
        return topK;
    }
}
```
