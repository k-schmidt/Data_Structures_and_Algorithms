# Merge Overlapping Intervals

Given an array (list) of intervals as input where each interval has a start and end timestamps. Input array is sorted by starting timestamps. You are required to merge overlapping intervals and return output array (list).

## Hints
+ Linear Scan

## Solution
Runtime Complexity - O(n)


Memory Complexity - O(1)

### Pseudocode

1. List of input intervals is given, and we'll keep merged intervals in output list
2. For each interval in the input list
    3. If input interval is overlapping with the last interval in output list then we'll merge these two intervals and update last interval of output list with merged interval.
    4. Otherwise, we'll add input interval to the output list.

### Implementation

``` python
def find_busy_intervals(v1):
    if v1 == None or len(v1) == 0:
        return None

    v2 = []
    v2.append(pair(v1[0].first, v1[0].second))

    for i in range(1, len(v1)):
        x1 = v1[i].first
        y1 = v1[i].second
        x2 = v2[len(v2) - 1].first
        y2 = v2[len(v2) - 1].second

        if y2 >= x1:
            v2[len(v2) - 1].second = max(y1, y2)
        else:
            v2.append(pair(x1, y1))

    return v2
```
