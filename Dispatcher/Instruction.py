from enum import IntEnum

class InstructionType(IntEnum):
    CREATEFILE = 0
    DELETEFILE = 1
    CPUUSAGE   = 2

class Instruction:
    def __init__(self, information = [0, 0, "A", 1, 0]):
        if (information[1] == 0) and (len(information) != 5):
            print("Wrong number of instruction definitions")
        if (information[1] == 1) and (len(information) != 4):
            print("Wrong number of instruction definitions")
        self.process_id = int(information[0])
        self.op_code = InstructionType(int(information[1]))
        self.file_name = information[2]
        if self.op_code == InstructionType.CREATEFILE:
            self.file_blocks = int(information[3])
            self.instruction_number = int(information[4])
        else:
            self.instruction_number = int(information[3])
