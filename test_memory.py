from MemoryManager.Memory import Memory
from ProcessManager.ProcessType import ProcType
from ProcessManager.Process import Process

mem = Memory()
# mem.print()

processes = [Process() for i in range(25)]
size = 5
pid = 0
for proc in processes:
    proc.type = ProcType.USER
    proc.memory_blocks = size
    proc.pid = pid
    pid += 1
    size += 15

for indx in range(5):
    processes[indx].type = ProcType.REALTIME

for proc in processes:
    offset = mem.canAllocate(proc)
    if (offset != -1):
        print("Allocating...", proc.pid, proc.type, proc.memory_blocks)
        mem.allocate(proc, offset)
        mem.print()
    else:
        print("Could not allocate")
