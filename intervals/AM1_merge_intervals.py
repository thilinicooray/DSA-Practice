
def get_merged_intervals(intervals):
    #sorted_intervals = sorted(intervals,key=lambda i:i[0])
    intervals.sort()
    merged_list = []

    def is_overlapping(a,b):
        return max(a[0],b[0]) < min(a[1],b[1])

    for interval in intervals:
        if merged_list and is_overlapping(merged_list[-1],interval):
            merged_list[-1][1] = max(merged_list[-1][1],interval[1])
        else:
            merged_list.append(interval)

    return merged_list

intervals = [[1,3],[2,6],[8,10],[15,18]]

print(get_merged_intervals(intervals))