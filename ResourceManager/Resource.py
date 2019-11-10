from enum import IntEnum

class ResourceType(IntEnum):
    MODEM = 0
    SCANNER = 1
    DRIVE = 2
    PRINTER = 3

class ResourceStatus(IntEnum):
    ALLOCATED = 0
    AVAILABLE = 1


class Resource:
    # Basic definitions of a resource
    def __init__(self, type, code):
        self.type = type
        self.code = code
        self.status = ResourceStatus.AVAILABLE

    # Check if the resource is allocated to a process
    def isAvailable(self):
        return True if self.status else False

    # Get the process to which the resource was allocated
    def getProcess(self):
        return self.process

    def allocate(self, process):
        self.process = process
        self.status = ResourceStatus.ALLOCATED

    def deallocate(self):
        self.process = None
        self.status = ResourceStatus.AVAILABLE
