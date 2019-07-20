class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        if not intervals:
            return []
        
        if len(intervals) <= 1:
            return intervals
        
        intervals.sort(key=lambda x: x[0])
        
        merged = []
        
        merged.append(intervals[0])
        
        for i in range(1, len(intervals)):
            if intervals[i][0] <= merged[-1][1] and intervals[i][1] >= merged[-1][1]:
                merged[-1][1] = intervals[i][1]
            elif intervals[i][0] <= merged[-1][1]:
                continue
            else:
                merged.append(intervals[i])
                
        return merged
            