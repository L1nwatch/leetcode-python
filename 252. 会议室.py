class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        busy_time = set()
        for begin,end in intervals:
            for i in range(begin,end):
                if i in busy_time:
                    return False
                else:
                    busy_time.add(i)
        return True