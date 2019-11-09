from enum import IntEnum

class MemoryType(IntEnum):
    REALTIME = 0
    USER     = 1

class MemoryUsed:
    def __init__(self, process, offset):
        self.process = process
        self.offset = offset

    def __eq__(self, other):
        if isinstance(other, MemoryUsed):
            return (self.process == other.process) and (self.offset == other.offset)

class Memory:
    def __init__(self):
        self.blocks = [0] * 1024
        self.total_blocks = 1024
        self.starting_blocks = {MemoryType.USER: 64,
                                MemoryType.REALTIME: 0}
        self.ending_blocks = {MemoryType.USER: 1024,
                                MemoryType.REALTIME: 64}
        self.empty_blocks = {MemoryType.USER: 960,
                             MemoryType.REALTIME: 64}
        self.occupiedSpace = {MemoryType.USER: [],
                              MemoryType.REALTIME: []}

    def allocate(self, process, offset):
        mem_type = MemoryType(process.type)
        for block_indx in range(offset, offset + process.memory_blocks):
            self.blocks[block_indx] = 1
        self.occupiedSpace[mem_type].append(MemoryUsed(process, offset))
        self.empty_blocks[mem_type] -= process.memory_blocks

    def deAllocate(self, process):
        mem_type = MemoryType(process.type)
        for space in self.occupiedSpace[mem_type]:
            if space.process == process:
                break
        for block_indx in range(space.offset, space.offset + process.memory_blocks):
            self.blocks[block_indx] = 0
        self.occupiedSpace[mem_type].remove(space)
        self.empty_blocks[mem_type] += process.memory_blocks

    def canAllocate(self, process):
        mem_type = MemoryType(process.type)
        if (self.empty_blocks[mem_type] >= process.memory_blocks):
            counter = 0
            for block_indx in range(self.starting_blocks[mem_type],
                                    self.ending_blocks[mem_type]):
                if (self.blocks[block_indx] == 0):
                    counter += 1
                else:
                    counter = 0
                if (counter >= process.memory_blocks):
                    return block_indx + 1 - process.memory_blocks
        return -1

    def getProcessSpace(self, process):
        mem_type = MemoryType(process.type)
        for space in self.occupiedSpace[mem_type]:
            if space.process == process:
                return space

    def getBlockOwner(self, block_indx):
        if (block_indx < self.ending_blocks[MemoryType.REALTIME]):
            mem_type = MemoryType.REALTIME
        else:
            mem_type = MemoryType.USER
        for space in self.occupiedSpace[mem_type]:
            if (block_indx >= space.offset) and \
               ( block_indx < (space.process.memory_blocks + space.offset) ):
               return space.process.pid
        return -1


    def print(self):
        for block_indx in range(0, len(self.blocks)):
            print(block_indx, self.blocks[block_indx], self.getBlockOwner(block_indx))
