
def is_all_attendable(meetings):
    meetings.sort()

    def is_overlapping(a,b):
        return max(a[0],b[0]) < min(a[1],b[1])

    for i in range(1,len(meetings)):
        if is_overlapping(meetings[i-1],meetings[i]):
            return False

    return True


meetings = [[1,5],[8,15],[3,7],[20,24]]

print('can a person attend all meetings :',is_all_attendable(meetings))

