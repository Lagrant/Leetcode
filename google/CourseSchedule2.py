from collections import defaultdict, deque
class Course:
    def __init__(self, id) -> None:
        self.id = id
        self.next = []
        self.prev = []
        self.taken = False
    def append_next(self, next):
        self.next.append(next)
    def append_prev(self, prev):
        self.prev.append(prev)
    
class Solution:
    def __init__(self) -> None:
        self.course_graph = defaultdict(object)

    def findOrder(self, numCourses: int, prerequisites):

        if (len(prerequisites)  == 0):
            return [i for i in range(numCourses)]

        for pre in prerequisites:
            if (pre[1] not in self.course_graph):
                self.course_graph[pre[1]] = Course(pre[1])
            self.course_graph[pre[1]].append_next(pre[0])
            if (pre[0] not in self.course_graph):
                self.course_graph[pre[0]] = Course(pre[0])
            self.course_graph[pre[0]].append_prev(pre[1])
        
        taken_course, course_lst = 0, []
        for cid in self.course_graph:
            if (len(self.course_graph[cid].prev) == 0 and not self.course_graph[cid].taken):
                t_course, c_lst = self.takeCourse(cid)
                taken_course += t_course
                course_lst.extend(c_lst)
                if (taken_course >= numCourses):
                    return course_lst
        
        if (len(course_lst) == len(self.course_graph.keys()) and taken_course < numCourses):
            for i in range(numCourses):
                if (i not in course_lst):
                    course_lst.append(i)
            return course_lst 
        
        return []

    def takeCourse(self, cid):
        taken_course = 1
        course_lst = [cid]
        course_que = deque([cid])
        # for c in course_lst:
        while(len(course_que) > 0):
            c = course_que.popleft()
            for nxt in self.course_graph[c].next:
                self.course_graph[nxt].prev.remove(c)
                if (len(self.course_graph[nxt].prev) == 0):
                    taken_course += 1
                    course_lst.append(nxt)
                    course_que.append(nxt)
                    self.course_graph[nxt].taken = True
                    if (taken_course >= 4):
                        return taken_course, course_lst
        return taken_course, course_lst
                
sol = Solution()
print(sol.findOrder(numCourses = 7, prerequisites = [[1,0],[0,3],[0,2],[3,2],[2,5],[4,5],[5,6],[2,4]]))