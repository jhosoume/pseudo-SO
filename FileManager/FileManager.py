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

	def create_file(self, disk, file_size, file_name, process_id):
		if file_size > disk.free_space:
			print("Disk out of space")
		else:
			block = self.find_block(disk, file_size)
			if block == -1:
				print("No contiguous blocks for file")
			else:
				for i in range(0, file_size):
					disk.blocks[block + i] = file_name
					self.file_owner[block + i] = -1
				disk.free_space = disk.free_space - file_size
				

	def delete_file(self, disk, file_name, process_type, process_id):
		try:
			block = disk.blocks.index(file_name)
		except ValueError:
			print("File does not exist")
		else:
			if (self.check_owner(disk, file_name) != process_id) and (process_type != 0):
				print("No permission to delete file")
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
		print("File Manager:")
		print("\tDisk Free Space:", disk.free_space)
		print("\tDisk Map:", disk.blocks)
		print("\tDisk Map Owners:", self.file_owner)

class HardDisk:
	def __init__(self, max_size):
		self.max_size = max_size
		self.free_space = max_size
		self.blocks = []
		for i in range(0, max_size):
			self.blocks.append(0)