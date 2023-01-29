# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import bisect

from typing import List

class SummaryRanges:
    def __init__(self):
        self.intervals = []

    def addNum(self, value: int) -> None:
        # Create a new interval for the given value
        new_interval = [value, value]

        # Find the position of the new interval in the list of intervals
        pos = bisect.bisect_left(self.intervals, new_interval)

        # Check if the new interval overlaps with the previous or the next interval
        if pos > 0 and self.intervals[pos-1][1] + 1 >= new_interval[0]:
            # The new interval overlaps with the previous interval
            # Update the previous interval with the new interval
            self.intervals[pos-1][1] = max(self.intervals[pos-1][1], new_interval[1])
            # Check if the updated previous interval also overlaps with the next interval
            if pos < len(self.intervals) and self.intervals[pos-1][1] + 1 >= self.intervals[pos][0]:
                # The updated previous interval overlaps with the next interval
                # Update the next interval with the updated previous interval
                self.intervals[pos][0] = self.intervals[pos-1][0]
                # Remove the updated previous interval from the list
                self.intervals.pop(pos-1)
        elif pos < len(self.intervals) and self.intervals[pos][0] <= new_interval[1] + 1:
            # The new interval overlaps with the next interval
            # Update the next interval with the new interval
            self.intervals[pos][0] = min(self.intervals[pos][0], new_interval[0])
        else:
            # The new interval does not overlap with any existing intervals
            # Insert the new interval at the correct position
            self.intervals.insert(pos, new_interval)

    def getIntervals(self) -> List[List[int]]:
        return self.intervals
    
    
