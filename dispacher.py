import sys
from Helper.Helper import *

PATH = "tests/"
PROCESSES_FILE = PATH + sys.argv[1]
FILES_FILE = PATH + sys.argv[2]

processes = Helper.read_processes(PROCESSES_FILE)
files = Helper.read_files(FILES_FILE)

pids = []
pid = 0
offset = 0
blocks = 0
priority = 0
time = 0
printers = 0
scanners = 0
modems = 0
drives = 0
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
            drives: {}""".format(pid,
                                 offset,
                                 blocks,
                                 priority,
                                 time,
                                 printers,
                                 scanners,
                                 modems,
                                 drives)
        )

