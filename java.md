1st

PriorityQueueのドキュメント：https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/PriorityQueue.html#add(E)

```python
class Solution {
    public int minMeetingRooms(int[][] intervals) {
        int maxOngoingMeetings = 0;
        int numOngoingMeetings = 0;
        PriorityQueue<Integer> meetingEndTimes = new PriorityQueue<>();

        Arrays.sort(intervals, (a, b) -> a[0] - b[0]);
        for (int i = 0; i < intervals.length; i++) {
            int startTime = intervals[i][0];
            int endTime = intervals[i][1];
            while (!meetingEndTimes.isEmpty() && meetingEndTimes.peek() <= startTime) {
                meetingEndTimes.poll();
                numOngoingMeetings -= 1;
            }
            numOngoingMeetings += 1;
            maxOngoingMeetings = Math.max(maxOngoingMeetings, numOngoingMeetings);
            meetingEndTimes.add(endTime);
        }
        return maxOngoingMeetings;
    }
}
```
