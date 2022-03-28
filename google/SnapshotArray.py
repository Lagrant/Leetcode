class SnapElement:
    def __init__(self, sp_id, val) -> None:
        self.his = {sp_id: val}
        # self.latest = [sp_id]
    
class SnapshotArray:
    def find_latest(self, sp_id, latest):
        l, r = 0, len(latest) - 1
        while (l < r):
            mid = (l + r) // 2
            if (latest[mid] > sp_id):
                r = mid - 1
            elif (latest[mid] < sp_id):
                l = mid + 1
        if (latest[r] < sp_id):
            return latest[r]
        else:
            return latest[r - 1]

    def __init__(self, length: int):
        self.snaps = [SnapElement(0, 0) for i in range(length)]
        self.snap_cnt = 0

    def set(self, index: int, val: int) -> None:
        # if self.snap_cnt not in self.snaps[index].his:
            # self.snaps[index].latest.append(self.snap_cnt)
        self.snaps[index].his[self.snap_cnt] = val

    def snap(self) -> int:
        self.snap_cnt += 1
        return self.snap_cnt - 1

    def get(self, index: int, snap_id: int) -> int:
        if snap_id in self.snaps[index].his:
            return self.snaps[index].his[snap_id]
        else:
            sp_id = self.find_latest(snap_id, list(self.snaps[index].his.keys()))
            return self.snaps[index].his[sp_id]


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)

obj = SnapshotArray(2)
obj.set(0, 12)
obj.snap()
obj.snap()
obj.get(1,0)
obj.get(1,0)
param_2 = obj.snap()
# param_3 = obj.set(1,4)
obj.snap()