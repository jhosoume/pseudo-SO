class Process:
    def __init__(self, information):
        self.pid = -1
        self.offset = -1

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

        try:
            self.cpu_time = int(information[2])
        except ValueError:
            print("Process cpu time not in the expected format.")
        if (self.cpu_time < 0):
            self.cpu_time = 0
            print("Process arrival time less than zero.")

        try:
            self.memory_blocks = int(information[3])
        except ValueError:
            print("Process memory blocks not in the expected format.")
        if (self.memory_blocks < 0):
            self.memory_blocks = 0
            print("Process memory blocks less than zero.")

        try:
            self.printer_code = int(information[4])
        except ValueError:
            print("Process printer code not in the expected format.")
        if (self.printer_code < 0 or self.printer_code > 2):
            self.printer_code = 0
            print("Process printer code less than zero.")

        try:
            self.req_scanner = int(information[5])
            if (self.req_scanner < 0 or self.req_scanner > 1):
                print("Process scanner requirement less than zero.")
            self.req_scanner = bool(self.req_scanner)
        except ValueError:
            print("Process scanner requirement not in the expected format.")

        try:
            self.req_modem = information[6]
            if (self.req_modem < 0 or self.req_modem > 1):
                print("Process modem requirement less than zero.")
            self.req_modem = bool(self.req_modem)
        except ValueError:
            print("Process modem requirement not in the expected format.")

        try:
            self.disk_code = information[7]
        except ValueError:
            print("Process disk code not in the expected format.")
        if (self.disk_code < 0 or self.disk_code > 2):
            self.disk_code = 0
            print("Process printer code blocks less than zero.")

        def assignPID(self, pid):
            self.pid = pid

        def assignOffset(self, offset):
            self.offset = offset
