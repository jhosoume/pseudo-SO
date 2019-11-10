import sys
from Helper.Helper import Helper
from Dispatcher.Dispatcher import Dispatcher
from MemoryManager.Memory import Memory
from FileManager.FileManager import *
from ProcessManager.Process import *
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
memory_manager = Memory()

# Create resource manager
resource_manager = ResourceManager()

# Create process manager
process_manager = ProcessQueue()

# Create disk and file manager
disk = HardDisk(dispatcher.file_blocks)
file_manager = FileManager(dispatcher.file_blocks)
# TODO initialize disk

control = len(dispatcher.processes)
while control > 0:

    # Add arriving process to queue
    for proc in dispatcher.processes:
        if proc.arrival_time == dispatcher.time:
            proc.setPID(dispatcher.pid)
            dispatcher.pid += 1
            process_manager.addProcess(proc)

    # See if there is an active process
    if dispatcher.active_process != None:
        if dispatcher.active_process.cpu_time == dispatcher.active_process.cpu_usage:
            resource_manager.deallocateAll(dispatcher.active_process)
            memory_manager.deAllocate(dispatcher.active_process)
            dispatcher.active_process = None
            control -= 1
        elif dispatcher.active_process.priority == 0:
            dispatcher.run_instruction(file_manager, disk)
            dispatcher.active_process.cpu_usage += 1
        else:
            process_manager.readdProcess(dispatcher.active_process)
            dispatcher.active_process = None
    if dispatcher.active_process == None and process_manager.queuesLen() > 0:
        # Get process from process queue
        for proc in process_manager.listInOrder():
            # Try allocation
            offset = memory_manager.canAllocate(proc)
            has_resources = resource_manager.canAllocate(proc)
            if offset >= 0 and has_resources:
                process_manager.remove(proc)
                memory_manager.allocate(proc,offset)
                resource_manager.allocateAllNeeded(proc)
                proc.setOffset(offset)
                proc.next_instr = [inst for inst in dispatcher.instructions if inst.process_id == proc.pid][:proc.cpu_time]
                dispatcher.active_process = proc
                break

        if dispatcher.active_process != None:
            # Run process
            dispatcher.print_process(proc)
            dispatcher.run_instruction(file_manager, disk)
            dispatcher.active_process.cpu_usage += 1

    dispatcher.time += 1
