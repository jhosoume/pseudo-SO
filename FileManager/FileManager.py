class FileManager:
	def __init__(self, max_size):
		self.file_owner = []
		for i in range(0, max_size):
			self.file_owner.append(-1)

	def insert_file(self, disk, file_name, first_block, file_size):
		for i in range(0, file_size):
			disk.blocks[first_block + i] = file_name
			self.file_owner[first_block + i] = -1
		disk.free_space = disk.free_space - file_size
		print("File Manager: File {} added to disk. Starting in block {} and size {}".format(file_name, first_block, file_size))

	def create_file(self, disk, file_size, file_name, process_id):
		if file_size > disk.free_space:
			print("Disk out of space for file {}".format(file_name))
		else:
			block = self.find_block(disk, file_size)
			if block == -1:
				print("File Manager: No contiguous blocks for file {}".format(file_name))
			else:
				for i in range(0, file_size):
					disk.blocks[block + i] = file_name
					self.file_owner[block + i] = -1
				disk.free_space = disk.free_space - file_size
				print("File Manager: File {} created. Starting in block {} and size {} by process {}".format(file_name, block, file_size, process_id))

	def delete_file(self, disk, file_name, process_type, process_id):
		try:
			block = disk.blocks.index(file_name)
		except ValueError:
			print("File Manager: File {} does not exist".format(file_name))
		else:
			if (self.check_owner(disk, file_name) != process_id) and (process_type != 0):
				print("File Manager: No permission to delete file {}".format(file_name))
			else:
				file_size = 0
				for i in range(block, disk.max_size):
					if disk.blocks[i] == file_name:
						file_size += 1
					else:
						break;
				for i in range(block, disk.max_size):
					if disk.blocks[i] == file_name:
						self.file_owner[i] = -1
						disk.blocks[i] = 0
					else:
						break;
				disk.free_space = disk.free_space + file_size
				print("File Manager: File {} deleted. Starting in block {} and size {} by process {}".format(file_name, block, file_size, process_id))

	def check_owner(self, disk, file_name):
		block = disk.blocks.index(file_name)

	def find_block(self, disk, file_size):
		counter = 0
		for i in range(0, disk.max_size):
			if disk.blocks[i] == 0:
				counter += 1
			else:
				counter = 0
			if counter >= file_size:
				return i + 1 - file_size
		return -1

	def show_disk(self, disk):
		print("File Manager: Disk status:")
		print("\tDisk Free Space:", disk.free_space)
		print("\tDisk Map:", disk.blocks)
		print("\tDisk Owners Map:", self.file_owner)

class HardDisk:
	def __init__(self, max_size):
		self.max_size = max_size
		self.free_space = max_size
		self.blocks = []
		for i in range(0, max_size):
			self.blocks.append(0)