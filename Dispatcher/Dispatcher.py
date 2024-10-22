from Helper.Helper import Helper
from ProcessManager.Process import Process
from Dispatcher.Instruction import *

class Dispatcher:
    def __init__(self, procs_file, files_file):
        self.processes_file = procs_file
        self.files_file = files_file
        self.pid = 0
        self.processes = []
        self.instructions = []
        self.time = 0
        self.active_process = None

    def load_processes(self):
        processes_array = Helper.read_processes(self.processes_file)
        self.processes = [Process(indx, item) for indx, item in enumerate(processes_array)]

    def load_instructions(self):
        files_array = Helper.read_files(self.files_file)
        self.file_blocks = int(files_array[0])
        num_files = int(files_array[1])
        self.files_to_initialize =  files_array[2:num_files + 2]
        self.instructions = [Instruction(item) for item in files_array[num_files + 2:]]

    def run_instruction(self, file_manager, disk):
        inst = [instruction for instruction in self.active_process.next_instr if instruction.instruction_number == self.active_process.cpu_usage]
        if len(inst) != 0:
            print("-> T{} - P{}: Instruction {} ".format(self.time, self.active_process.pid, self.active_process.cpu_usage))
            if inst[0].op_code == 0:
                file_manager.create_file(disk,inst[0].file_blocks,inst[0].file_name, self.active_process.pid)
            elif inst[0].op_code ==  1:
                file_manager.delete_file(disk, inst[0].file_name, self.active_process.type, self.active_process.pid)
        else:
            print("-> T{} - P{}: Instruction {} SUCCESS CPU".format(self.time, self.active_process.pid, self.active_process.cpu_usage))

    def print_process(self, proc):
        print(
        """dispatcher =>
            PID: {}
            ID: {}
            offset: {}
            blocks: {}
            priority: {}
            CPU time: {}
            printers: {}
            scanners: {}
            modems: {}
            drives: {}""".format(proc.pid,
                                 proc.id,
                                 proc.offset,
                                 proc.memory_blocks,
                                 proc.priority,
                                 proc.cpu_time,
                                 proc.printer_code,
                                 proc.req_scanner,
                                 proc.req_modem,
                                 proc.drive_code)
            )
