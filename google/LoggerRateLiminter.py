from collections import OrderedDict
class Logger:

    def __init__(self):
        # self.messg_que = OrderedDict()
        self.messg_que = {}
        # self.messg_cnt = 0

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        flag = False
        if (message not in self.messg_que):
            self.messg_que[message] = timestamp
            flag = True
            # self.messg_cnt += 1
            # if (self.messg_cnt > 10):
            #     self.messg_que.popitem(last=True)
            #     self.messg_cnt -= 1
        elif (timestamp - 10 >= self.messg_que[message]):
            flag = True
            self.messg_que[message] = timestamp
            
        return flag
        


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)