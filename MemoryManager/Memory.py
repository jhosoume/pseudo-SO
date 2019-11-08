from enum import IntEnum

class MemoryType(IntEnum):
    REALTIME = 0
    USER     = 1

class MemorySegment:
    def __init__(self, process, offset, num_blocks):
        self.process = process
        self.offset = offset
        self.num_blocks = num_blocks

class Memory:
    def __init__(self):
        self.blocks = [0] * 1024
        self.total_blocks = 1024
        self.empty_realtime = 64
        self.empty_user = 960
        self.empty_blocks = self.empty_realtime + self.empty_user
        self.occupiedUserSpace = []
        self.occupiedRealTimeSpace = []

    def allocate(self, process):
        pass

    def canAllocate(self, process):
        pass

    def deAllocate(self, process):
        pass
        
