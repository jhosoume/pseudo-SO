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
for file in dispatcher.files_to_initialize:
	file_manager.insert_file(disk, file[0], int(file[1]), int(file[2]))

control = len(dispatcher.processes)
while control > 0:
	# import pdb; pdb.set_trace()
	# Add arriving process to queue
	for proc in dispatcher.processes:
		if proc.arrival_time == dispatcher.time:
			if proc.memory_blocks > memory_manager.num_blocks[proc.type]:
				print("Process of ID ", proc.id, " require more memory blocks than memory maximum size!")
				continue
			proc.setPID(dispatcher.pid)
			dispatcher.pid += 1
			process_manager.addProcess(proc)
	# pdb.set_trace()
	# resource_manager.print_devices()
	# See if there is an active process
	memory_manager.show_info()
	if dispatcher.active_process != None:
		if dispatcher.active_process.cpu_time == dispatcher.active_process.cpu_usage:
			if (len(dispatcher.active_process.next_instr[dispatcher.active_process.cpu_time:]) > 0):
				print("Could not execute instructions",
					   [inst.instruction_number for inst in dispatcher.active_process.next_instr[dispatcher.active_process.cpu_time:]],
					   " CPU Time Exceeded!")
			resource_manager.deallocateAll(dispatcher.active_process)
			memory_manager.deAllocate(dispatcher.active_process)
			dispatcher.active_process = None
			control -= 1
		elif dispatcher.active_process.priority == 0:
			dispatcher.run_instruction(file_manager, disk)
			dispatcher.active_process.cpu_usage += 1
			file_manager.show_disk(disk)
		else:
			process_manager.readdProcess(dispatcher.active_process)
			dispatcher.active_process = None

	# pdb.set_trace()
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
				proc.next_instr = [inst for inst in dispatcher.instructions if inst.process_id == proc.id]
				dispatcher.active_process = proc
				file_manager.show_disk(disk)
				break

		# pdb.set_trace()
		if dispatcher.active_process != None:
			# Run process
			dispatcher.print_process(proc)
			dispatcher.run_instruction(file_manager, disk)
			dispatcher.active_process.cpu_usage += 1
			# pdb.set_trace()
		else:
			print("DEADLOCK!")
			quit()

	dispatcher.time += 1
