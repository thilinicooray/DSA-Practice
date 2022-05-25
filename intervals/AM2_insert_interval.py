
def get_new_intervals(intervals, newInterval):

    if not intervals:
        return [newInterval]

    updated_intervals = []
    def is_overlapping(a,b):
        return max(a[0],b[0]) <= min(a[1],b[1])
    i = 0
    while i < len(intervals):

        if not is_overlapping(intervals[i],newInterval):
            updated_intervals.append(intervals[i])
            i += 1
        else:
            while i < len(intervals) and is_overlapping(intervals[i],newInterval):
                newInterval = [min(intervals[i][0],newInterval[0]),max(intervals[i][1],newInterval[1])]
                i += 1

            updated_intervals.append(newInterval)

    return updated_intervals


#intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
#newInterval = [4,8]
intervals = [[1,5]]
newInterval = [2,3]

print(get_new_intervals(intervals, newInterval))