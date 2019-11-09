from ResourceManager.Resouce import *

class ResourceManager:
    def __init__(self):
        self.resources = {
            ResourceType.MODEM: Resouce(ResourceType.MODEM, 1),
            ResourceType.SCANNER: Resouce(ResourceType.SCANNER, 1),
            ResourceType.DRIVE: {
                1: Resource(ResourceType.DRIVE, 1),
                2: Resource(ResourceType.DRIVE, 2),
            },
            ResourceType.PRINTER: {
                1: Resource(ResourceType.PRINTER, 1),
                2: Resource(ResourceType.PRINTER, 2),
            }
        }

    def canAllocate(self, process):
        return False

    def allocateAllNeeded(self, process):
        return NotImplemented

    def deallocateAll(self, process):
        return NotImplemented
