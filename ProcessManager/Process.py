from ProcessManager.ProcessType import ProcType

class Process:
    # Information order:
    #   1. Arrival Time
    #   2. Priority
    #   3. CPU Time
    #   4. Memory Blocks
    #   5. Printer Code
    #   6. Req Scanner
    #   7. Req Modem
    #   8. Drive Code
    def __init__(self, information = [0, 0, 1, 1, 0, 0, 0, 0]):
        self.pid = -1
        self.offset = -1
        self.next_instr = None

        # Information is a list of all process info
        if (len(information) != 8):
            print("Array of process information not with enough attributes")

        try:
            self.arrival_time = int(information[0])
        except ValueError:
            self.arrival_time = 0
            print("Process arrival time not in the expected format.")

        if (self.arrival_time < 0):
            self.arrival_time = 0
            print("Process arrival time less than zero.")

        try:
            priority = int(information[1])
        except ValueError:
            print("Process priority not in the expected format.")
        if (priority > 3 or priority < 0):
            priority = 3
            print("Process priority not within range.")
        self.priority = priority

        if (self.priority == 0):
            self.type = ProcType.REALTIME
        else:
            self.type = ProcType.USER

        try:
            self.cpu_time = int(information[2])
        except ValueError:
            print("Process cpu time not in the expected format.")
        if (self.cpu_time < 0):
            self.cpu_time = 0
            print("Process cpu time less than zero.")

        try:
            self.memory_blocks = int(information[3])
        except ValueError:
            print("Process memory blocks not in the expected format.")
        if (self.memory_blocks < 0):
            self.memory_blocks = 0
            print("Process memory blocks less than zero.")

        try:
            self.printer_code = int(information[4])
            self.req_printer = True if self.printer_code > 0 else False
        except ValueError:
            print("Process printer code not in the expected format.")
        if (self.printer_code < 0 or self.printer_code > 2):
            self.printer_code = 0
            self.req_printer = False
            print("Process printer code less than zero.")

        try:
            self.req_scanner = int(information[5])
            if (self.req_scanner < 0 or self.req_scanner > 1):
                print("Process scanner requirement less than zero.")
            self.req_scanner = bool(self.req_scanner)
        except ValueError:
            print("Process scanner requirement not in the expected format.")

        try:
            self.req_modem = int(information[6])
            if (self.req_modem < 0 or self.req_modem > 1):
                print("Process modem requirement less than zero.")
            self.req_modem = bool(self.req_modem)
        except ValueError:
            print("Process modem requirement not in the expected format.")

        try:
            self.drive_code = int(information[7])
            self.req_drive = True if self.drive_code > 0 else False
        except ValueError:
            print("Process disk code not in the expected format.")
        if (self.drive_code < 0 or self.drive_code > 2):
            self.drive_code = 0
            self.req_drive = False
            print("Process printer code blocks less than zero.")

    def __eq__(self, other):
        if isinstance(other, Process):
            return self.pid == other.pid
        return NotImplemented

    def setPID(self, pid):
        self.pid = pid

    def setOffset(self, offset):
        self.offset = offset

    def setNextInstr(self, instruction):
        self.next_instr = instruction
