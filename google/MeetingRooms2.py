from typing import List
import heapq
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
    
    def minMeetingRooms2(self, intervals: List[List[int]]) -> int:
        
        # If there is no meeting to schedule then no room needs to be allocated.
        if not intervals:
            return 0

        # The heap initialization
        free_rooms = []

        # Sort the meetings in increasing order of their start time.
        intervals.sort(key= lambda x: x[0])

        # Add the first meeting. We have to give a new room to the first meeting.
        heapq.heappush(free_rooms, intervals[0][1])

        # For all the remaining meeting rooms
        for i in intervals[1:]:

            # If the room due to free up the earliest is free, assign that room to this meeting.
            if free_rooms[0] <= i[0]:
                heapq.heappop(free_rooms)

            # If a new room is to be assigned, then also we add to the heap,
            # If an old room is allocated, then also we have to add to the heap with updated end time.
            heapq.heappush(free_rooms, i[1])

        # The size of the heap tells us the minimum rooms required for all the meetings.
        return len(free_rooms)

sol = Solution()
print(sol.minMeetingRooms([[0,30],[5,10],[15,20]]))