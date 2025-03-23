def mergeIntervals(intervals: list[tuple[int, int]]) -> list[tuple[int, int]]:
    if not intervals:
        return []
    
    overLappedIntervals = []
    intervals.sort(key=lambda x: x[0])
    overLappedIntervals.append(intervals[0])
    
    for idx in range(1, len(intervals)):
        if overLappedIntervals[-1][1] >= intervals[idx][0]:
            overLappedIntervals[-1] = (overLappedIntervals[-1][0], intervals[idx][1])
        else:
            overLappedIntervals.append(intervals[idx])
    
    return overLappedIntervals

    
intervals = [(2, 3), (4, 8), (1, 2), (5, 7), (9, 12)]
print(mergeIntervals(intervals))

intervals = [(5, 8), (6, 10), (2, 4), (3, 6)]
print(mergeIntervals(intervals))

intervals = [(10, 12), (5, 6), (7, 9), (1, 3)]
print(mergeIntervals(intervals))

