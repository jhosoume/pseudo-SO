from enum import IntEnum

class InstructionType(IntEnum):
    CREATEFILE = 0
    DELETEFILE = 1
    CPUUSAGE   = 2

class Instruction:
    def __init__(self, information = [0, 0, "A", 1, 0]):
        if (infomation[1] == 0) and (len(information) != 5):
            print("wrong number of instruction definitions")
        if (infomation[1] == 1) and (len(information) != 4):
            print("wrong number of instruction definitions")
        self.process_id = information[0]
        self.op_code = InstructionType(information[1])
        self.file_name = information[2]
        if self.op_code == InstructionType.CREATEFILE:
            self.file_blocks = information[3]
        self.instruction_number = infomation[4]
