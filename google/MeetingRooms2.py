class timeClock:
    def __init__(self, id, time, begin) -> None:
        self.id = id
        self.time = time
        self.begin = begin

class Solution:
    def minMeetingRooms(self, intervals) -> int:
        times = []
        for i, interv in enumerate(intervals):
            times.append(timeClock(i, interv[0], 0))
            times.append(timeClock(i, interv[1], -0.5))
        
        times.sort(key=lambda x: x.time + x.begin)

        using_room, max_room = 0, 1
        for t in times:
            if (t.begin == 0):
                using_room +=1
                max_room = using_room if (using_room > max_room) else max_room
            else:
                using_room -= 1
        return max_room

sol = Solution()
print(sol.minMeetingRooms([[0,30],[5,10],[15,20]]))