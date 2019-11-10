from ResourceManager.Resource import *

class ResourceManager:
    def __init__(self):
        # Initalize all resources types
        self.resources = {
            ResourceType.MODEM: Resource(ResourceType.MODEM, 1),
            ResourceType.SCANNER: Resource(ResourceType.SCANNER, 1),
            ResourceType.DRIVE: {
                1: Resource(ResourceType.DRIVE, 1),
                2: Resource(ResourceType.DRIVE, 2),
            },
            ResourceType.PRINTER: {
                1: Resource(ResourceType.PRINTER, 1),
                2: Resource(ResourceType.PRINTER, 2),
            }
        }

    # Check if every resource required from the process is free
    def canAllocate(self, process):
        if process.req_modem:
            if not self.resources[ResourceType.MODEM].isAvailable():
                return False
        if process.req_scanner:
            if not self.resources[ResourceType.SCANNER].isAvailable():
                return False
        if process.req_drive:
            if not self.resources[ResourceType.DRIVE][process.drive_code].isAvailable():
                return False
        if process.req_printer:
            if not self.resources[ResourceType.PRINTER][process.printer_code].isAvailable():
                return False
        return True

    # Allocates the resources to the process
    def allocateAllNeeded(self, process):
        if process.req_modem:
            self.resources[ResourceType.MODEM].allocate(process)
        if process.req_scanner:
            self.resources[ResourceType.SCANNER].allocate(process)
        if process.req_drive:
            self.resources[ResourceType.DRIVE][process.drive_code].allocate(process)
        if process.req_printer:
            self.resources[ResourceType.PRINTER][process.printer_code].allocate(process)

    # Deallocates the resources to the process
    def deallocateAll(self, process):
        if process.req_modem:
            self.resources[ResourceType.MODEM].deallocate()
        if process.req_scanner:
            self.resources[ResourceType.SCANNER].deallocate()
        if process.req_drive:
            self.resources[ResourceType.DRIVE][process.drive_code].deallocate()
        if process.req_printer:
            self.resources[ResourceType.PRINTER][process.printer_code].deallocate()

    def print_devices(self):
        print("---------------------------------------------")
        print("------------- RESOURCE MANAGER --------------")
        print("Modem: ")
        print(" Available = ", self.resources[ResourceType.MODEM].isAvailable())
        if not self.resources[ResourceType.MODEM].isAvailable():
            pid = self.resources[ResourceType.MODEM].process.pid
        else:
            pid = -1
        print(" Process PID = ", pid)
        print("Scanner: ")
        print(" Available = ", self.resources[ResourceType.SCANNER].isAvailable())
        if not self.resources[ResourceType.SCANNER].isAvailable():
            pid = self.resources[ResourceType.SCANNER].process.pid
        else:
            pid = -1
        print(" Process PID = ", pid)
        print("Drive of code", 1, ":")
        print(" Available = ", self.resources[ResourceType.DRIVE][1].isAvailable())
        if not self.resources[ResourceType.DRIVE][1].isAvailable():
            pid = self.resources[ResourceType.DRIVE][1].process.pid
        else:
            pid = -1
        print(" Process PID = ", pid)
        print("Drive of code", 2, ":")
        print(" Available = ", self.resources[ResourceType.DRIVE][2].isAvailable())
        if not self.resources[ResourceType.DRIVE][2].isAvailable():
            pid = self.resources[ResourceType.DRIVE][2].process.pid
        else:
            pid = -1
        print(" Process PID = ", pid)
        print("Printer of code", 1, ":")
        print(" Available = ", self.resources[ResourceType.PRINTER][1].isAvailable())
        if not self.resources[ResourceType.PRINTER][1].isAvailable():
            pid = self.resources[ResourceType.PRINTER][1].process.pid
        else:
            pid = -1
        print(" Process PID = ", pid)
        print("Printer of code", 2, ":")
        print(" Available = ", self.resources[ResourceType.PRINTER][2].isAvailable())
        if not self.resources[ResourceType.PRINTER][2].isAvailable():
            pid = self.resources[ResourceType.PRINTER][2].process.pid
        else:
            pid = -1
        print(" Process PID = ", pid)
        print("---------------------------------------------")
