from FileManager.FileManager  import HardDisk
from FileManager.FileManager import FileManager

disk_max_size = 10

disk = HardDisk(disk_max_size)
file_manager = FileManager(disk_max_size)

file_manager.create_file(disk, 2, "A", 1)

file_manager.show_disk(disk)

file_manager.create_file(disk, 4, "B", 2)

file_manager.show_disk(disk)

file_manager.create_file(disk, 3, "C", 3)

file_manager.show_disk(disk)

file_manager.create_file(disk, 1, "D", 2)

file_manager.show_disk(disk)

file_manager.delete_file(disk, "A", 0, 1)

file_manager.show_disk(disk)

file_manager.delete_file(disk, "C", 0, 3)

file_manager.show_disk(disk)

file_manager.create_file(disk, 5, "E", 1)

file_manager.show_disk(disk)

file_manager.delete_file(disk, "B", 1, 3)

file_manager.show_disk(disk)

file_manager.insert_file(disk, "Z", 6, 3)

file_manager.show_disk(disk)