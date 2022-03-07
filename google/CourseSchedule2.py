from collections import defaultdict, deque
class Solution:
    def __init__(self) -> None:
        self.course_graph = defaultdict(dict)

    def findOrder(self, numCourses: int, prerequisites):

        if (len(prerequisites)  == 0):
            return list(range(numCourses))

        for pre in prerequisites:
            if (pre[1] not in self.course_graph):
                self.course_graph[pre[1]] = {'next': [pre[1]], 'prev': 0}
            self.course_graph[pre[1]]['next'].append(pre[0])
            if (pre[0] not in self.course_graph):
                self.course_graph[pre[0]] = {'next': [pre[0]], 'prev': 0}
            self.course_graph[pre[0]]['prev'] += 1
        
        course_lst = []
        course_que = deque([])
        for cid in range(numCourses):
            if (cid not in self.course_graph):
                course_lst.append(cid)
            elif (self.course_graph[cid]['prev'] == 0):
                course_que.append(cid)

        if (len(course_que) == 0):
            return []

        c_lst = self.takeCourse(course_que)
        taken_course = len(c_lst) + len(course_lst)
        course_lst.extend(c_lst)
        if (taken_course >= numCourses):
            return course_lst
        
        return []

    def takeCourse(self, course_que):
        course_lst = []
        while(len(course_que) > 0):
            c = course_que.popleft()
            course_lst.append(c)
            for nxt in self.course_graph[c]['next']:
                self.course_graph[nxt]['prev'] -= 1
                if (self.course_graph[nxt]['prev'] == 0):
                    course_que.append(nxt)
        return course_lst
                
sol = Solution()
print(sol.findOrder(numCourses = 3, prerequisites = [[2,0],[2,1]]))