import sys
from Helper.Helper import Helper
from Dispatcher.Dispatcher import Dispatcher
from MemoryManager.Memory import Memory
from FileManager.FileManager import *
from ProcessManager.ProcessManager import *
from ResourceManager.ResourceManager import *
from Queues.ProcessQueue import ProcessQueue

# Input Files
PROCESSES_FILE = sys.argv[1]
FILES_FILE = sys.argv[2]

# Create Dispatcher
dispatcher = Dispatcher(PROCESSES_FILE, FILES_FILE)
dispatcher.load_processes()
dispatcher.load_instructions()

# Create memory manager
memory = Memory()

# Create process queue
process_queue = ProcessQueue()

resource_manager = ResourceManager()

file_manager = FileManager()

while len(dispatcher.processes) > 0:
    print(dispatcher.time)

    # Add arriving process to queue
    proc = dispatcher.processes[0]
    if proc.arrival_time == dispatcher.time:
        proc.pid = dispatcher.pid
        dispatcher.pid += 1
        offset = memory.canAllocate(proc)
        if offset >= 0:
            memory.allocate(proc,offset)
            proc.offset = offset
            dispatcher.print_process(proc)
            memory.deAllocate(proc)
        process_queue.addProcess(proc)
        dispatcher.processes = dispatcher.processes[1:]

    # Check process queue
    p = process_queue.getProcess()
    if p.pid != -1:
        print("O processo {} está na CPU".format(p.pid))
    dispatcher.time += 1
