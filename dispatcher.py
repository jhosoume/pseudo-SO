import sys
from Helper.Helper import Helper
from Dispatcher.Dispatcher import Dispatcher

# Input Files
PROCESSES_FILE = sys.argv[1]
FILES_FILE = sys.argv[2]

# Create Dispatcher
dispatcher = Dispatcher(PROCESSES_FILE, FILES_FILE)
dispatcher.load_processes()

# Read Input Files
files_array = Helper.read_files(FILES_FILE)

print(len(dispatcher.processes))
for proc in dispatcher.processes:
    print(
            """dispatcher =>
                PID: {}
                offset: {}
                blocks: {}
                priority: {}
                time: {}
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
