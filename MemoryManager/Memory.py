from enum import IntEnum

# Define Memory Types and default values
class MemoryType(IntEnum):
    REALTIME = 0
    USER     = 1

# Structure to define occupied space to easily check memory being used
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

    # Allocates memory space to process starting in the offset
    def allocate(self, process, offset):
        mem_type = MemoryType(process.type)
        for block_indx in range(offset, offset + process.memory_blocks):
            self.blocks[block_indx] = 1
        # Add to the list of occupied space
        self.occupiedSpace[mem_type].append(MemoryUsed(process, offset))
        # Decrement number of empty blocks
        self.empty_blocks[mem_type] -= process.memory_blocks

    # Deallocates memory space from process
    def deAllocate(self, process):
        mem_type = MemoryType(process.type)
        # find space that the process occupies
        for space in self.occupiedSpace[mem_type]:
            if space.process == process:
                break
        # set blocks as unused
        for block_indx in range(space.offset, space.offset + process.memory_blocks):
            self.blocks[block_indx] = 0
        # remove from list of occupied spaces
        self.occupiedSpace[mem_type].remove(space)
        # adds to empty blocks
        self.empty_blocks[mem_type] += process.memory_blocks

    # Checks if there are contiguos free blocks to store process and returns the offset
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

    # Get the occupied space of a block
    def getProcessSpace(self, process):
        mem_type = MemoryType(process.type)
        for space in self.occupiedSpace[mem_type]:
            if space.process == process:
                return space
    # Get owners of blocks
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

    # Prints blocks with their owners
    def print(self):
        for block_indx in range(0, len(self.blocks)):
            print(block_indx, self.blocks[block_indx], self.getBlockOwner(block_indx))
