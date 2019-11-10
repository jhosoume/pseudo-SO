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

    def load_processes(self):
        processes_array = Helper.read_processes(self.processes_file)
        self.processes = [Process(item) for item in processes_array]

    def load_instructions(self):
        files_array = Helper.read_files(self.files_file)
        self.file_blocks = int(files_array[0])
        num_files = int(files_array[1])
        self.files_to_initialize =  files_array[2:num_files + 2]
        self.instructions = [Instruction(item) for item in files_array[num_files + 2:]]

    def print_process(self, proc):
        print(
        """dispatcher =>
            PID: {}
            offset: {}
            blocks: {}
            priority: {}
            CPU time: {}
            printers: {}
            scanners: {}
            modems: {}
            drives: {}""".format(proc.pid,
                                 proc.offset,
                                 proc.memory_blocks,
                                 proc.priority,
                                 proc.cpu_time,
                                 proc.printer_code,
                                 proc.req_scanner,
                                 proc.req_modem,
                                 proc.drive_code)
            )
