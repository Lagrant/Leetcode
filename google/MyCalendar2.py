class MyCalendarTwo:

    def __init__(self):
        self.single_intervs = []
        self.double_intervs = []
        # self.single_root = None
        # self.double_root = None

    def find_double(self, interval):
        start, end = interval
        for interv in self.double_intervs:
            # if (interv[0] <= start and start < interv[1] or\
            #     interv[0] < end and end <= interv[1]):
            #     return True
            if ( not (start >= interv[1] or end <= interv[0])):
                return True
        return False

    def insert_double(self, interval):
        start, end = interval
        for interv in self.single_intervs:
            # if (interv[0] <= start and start < interv[1] or\
            #     interv[0] < end and end <= interv[1]):
            if ( not (start >= interv[1] or end <= interv[0])):
                self.double_intervs.append([max(start, interv[0]), min(end, interv[1])])

    def insert_single(self, interval):
        self.single_intervs.append(interval)

    def insert_single1(self,interval):
        start, end = interval
        if (self.single_root is None):
            self.single_root = TimeInterv(start, end)
            return True
        
        cur = self.single_root
        double_start, double_end = -1, -1
        while (cur is not None):
            if (start > cur.end):
                if (cur.next is None):
                    cur.next = TimeInterv(start, end)
                    return True
                else:
                    cur = cur.next
            if (start < cur.start):
                double_start = cur.start
                cur.end = cur.start
                cur.start = start


    def book(self, start: int, end: int) -> bool:
        if (self.find_double([start, end])):
            return False
        else:
            self.insert_double([start, end])
            self.insert_single([start, end])
            
            return True


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)