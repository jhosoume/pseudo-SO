from ResourceManager.ResourceManager import *
from ProcessManager.Process import *

rec_manager = ResourceManager()

#                                 P  S  M  D
processes = [Process([0, 1, 1, 1, 1, 0, 0, 2]),
             Process([0, 1, 1, 1, 2, 1, 1, 1]),
             Process([0, 1, 1, 1, 1, 0, 0, 0]),
             Process([0, 1, 1, 1, 1, 0, 0, 2]),
             Process([0, 1, 1, 1, 1, 0, 0, 2])]
pid = 0
for proc in processes:
    proc.pid = pid
    pid += 1

for proc in processes[:3]:
    if (rec_manager.canAllocate(proc)):
        print("Allocating resource...")
        rec_manager.allocateAllNeeded(proc)
    else:
        print("Cannot allocate resource")
    rec_manager.print_devices()

rec_manager.deallocateAll(processes[0])
rec_manager.print_devices()

proc = processes[2]
if (rec_manager.canAllocate(proc)):
    print("Allocating resource...")
    rec_manager.allocateAllNeeded(proc)
else:
    print("Cannot allocate resource")
rec_manager.print_devices()
