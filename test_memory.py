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

processes[-2].memory_blocks = 85

for indx in range(5):
    processes[indx].type = ProcType.REALTIME
processes[2].memory_blocks += 4

for proc in processes:
    offset = mem.canAllocate(proc)
    if (offset != -1):
        print("Allocating...", proc.pid, proc.type, proc.memory_blocks)
        mem.allocate(proc, offset)
        # mem.print()
    else:
        print("Could not allocate", proc.pid)

mem.deAllocate(processes[8])
# mem.print()
proc_1 = Process()
proc_1.type = ProcType.USER
proc_1.pid = 99
proc_1.memory_blocks = 15
offset = mem.canAllocate(proc_1)
if (offset != -1):
    print("Allocating", proc_1.pid, offset)
    mem.allocate(proc_1, offset)
    # mem.print()
else:
    print("Could not allocate", proc_1.pid)

mem.deAllocate(processes[11])
proc_2 = Process()
proc_2.type = ProcType.USER
proc_2.pid = 80
proc_2.memory_blocks = 120
offset = mem.canAllocate(proc_2)
if (offset != -1):
    print("Allocating", proc_2.pid, offset)
    mem.allocate(proc_2, offset)
else:
    print("Could not allocate", proc_2.pid)

proc_3 = Process()
proc_3.type = ProcType.USER
proc_3.pid = 77
proc_3.memory_blocks = 5
offset = mem.canAllocate(proc_3)
if (offset != -1):
    print("Allocating", proc_3.pid, offset)
    mem.allocate(proc_3, offset)
else:
    print("Could not allocate", proc_3.pid)

proc_4 = Process()
proc_4.type = ProcType.USER
proc_4.pid = 22
proc_4.memory_blocks = 105
offset = mem.canAllocate(proc_4)
if (offset != -1):
    print("Allocating", proc_4.pid, offset)
    mem.allocate(proc_4, offset)
else:
    print("Could not allocate", proc_4.pid)
mem.print()
