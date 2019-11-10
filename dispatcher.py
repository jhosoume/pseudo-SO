import sys
from Helper.Helper import Helper
from Dispatcher.Dispatcher import Dispatcher
from MemoryManager.Memory import Memory
from FileManager.FileManager import *
from ProcessManager.Process import *
from ResourceManager.ResourceManager import *
from Queues.ProcessQueue import ProcessQueue
from ResourceManager.ResourceManager import ResourceManager
from FileManager.FileManager import FileManager

# Input Files
PROCESSES_FILE = sys.argv[1]
FILES_FILE = sys.argv[2]

# Create Dispatcher
dispatcher = Dispatcher(PROCESSES_FILE, FILES_FILE)
dispatcher.load_processes()

# Read Input Files
dispatcher.load_instructions()

# Create memory manager
memory = Memory()

# Create resource manager
resource = ResourceManager()

# Create process queue
process_queue = ProcessQueue()

resource_manager = ResourceManager()

file_manager = FileManager(dispatcher.file_blocks)

while len(dispatcher.processes) > 0:
    print(dispatcher.time)

    # Add arriving process to queue
    for proc in dispatcher.processes:
        if proc.arrival_time <= dispatcher.time:
            proc.setPID(dispatcher.pid)
            dispatcher.pid += 1
            process_queue.addProcess(proc)

    # Get process from process queue
    successful = False
    proc_2_run = process_queue.getProcess()
    while not successful and proc_2_run.pid >= 0:
        if proc_2_run.pid >= 0:

            # Try allocation
            offset = memory.canAllocate(proc_2_run)
            has_resources = resource.canAllocate(proc_2_run)
            if offset >= 0 and has_resources:
                memory.allocate(proc_2_run,offset)
                resource.allocateAllNeeded(proc_2_run)
                proc_2_run.setOffset(offset)
                successful = True
            else:
                proc_2_run = process_queue.getProcess()
                process_queue.addProcess(proc_2_run)

    # Run process
    if successful:
        dispatcher.print_process(proc_2_run)
        insts = [x for x in dispatcher.instructions if int(x[0]) == proc_2_run.pid]
        if proc_2_run.priority == 0:
            max_i = min(proc_2_run.cpu_time, len(insts))
            for i in range(max_i):
                insts = [x for x in insts_array if int(x[0]) == proc_2_run.pid]
                print("{} Running instruction {}".format(dispatcher.time,insts[i]))
                dispatcher.time += 1
            memory.deAllocate(proc_2_run)
            dispatcher.processes = dispatcher.processes[1:]
        else:
            dispatcher.time += 1
    else:
        dispatcher.time += 1
