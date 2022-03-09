class Solution:
    def peakIndexInMountainArray(self, arr) -> int:
        start, end = 0, len(arr) - 1
        idx = int((start + end) / 2)
        while (end - start > 1):
            if (arr[idx] > arr[idx - 1] and arr[idx] > arr[idx + 1]):
                return idx
            elif (arr[idx - 1] < arr[idx] and arr[idx] < arr[idx + 1]):
                start = idx
            elif (arr[idx - 1] > arr[idx] and arr[idx] > arr[idx + 1]):
                end = idx
            
            idx = int((start + end) / 2)
        if (arr[start] > arr[start - 1] and arr[start] > arr[start + 1]):
            return start
        if (arr[end] > arr[end - 1] and arr[end] > arr[end + 1]):
            return end

sol = Solution()
print(sol.peakIndexInMountainArray([0,10,5,2]))