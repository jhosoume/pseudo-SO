from enum import IntEnum

class InstructionType(IntEnum):
    CREATEFILE = 0
    DELETEFILE = 1
    CPUUSAGE   = 2

class Instruction:
    def __init__(self, information = [0, 0, "A", 0]):
        pass
