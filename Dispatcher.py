from Helper.Helper import Helper
from ProcessManager.Process import Process

class Dispatcher:
    def __init__(self, procs_file, files_file):
        self.processes_file = procs_file
        self.files_file = files_file
        self.pid = 0
        self.processes = []

    def load_processes(self):
        processes_array = Helper.read_processes(self.processes_file)
        self.processes = [Process(item) for item in processes_array]

