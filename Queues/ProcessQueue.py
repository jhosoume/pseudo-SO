from collections import deque

class ProcessQueue():
	def __init__(self):
		self.queue = [deque(), deque(), deque(), deque()]

	def queuesLen(self):
		return len(self.queue[0]) + len(self.queue[1]) + len(self.queue[2]) + len(self.queue[3])

	def addProcess(self, process):
		queues_size = self.queuesLen()
		if queues_size < 1000:
			self.queue[process.priority].append(process)
		else:
			print("Excedeu tamanho limite das filas")

	def readdProcess(self, process):
		if process.priority < 3:
			process.priority = process.priority + 1
		self.addProcess(process)

	def removeProcess(self, priority):
		pass

	def printQueues(self):
		print("Tamanho da fila 0:", len(self.queue[0]))
		print("Tamanho da fila 1:", len(self.queue[1]))
		print("Tamanho da fila 2:", len(self.queue[2]))
		print("Tamanho da fila 3:", len(self.queue[3]))
		print("Tamanho total das filas:", self.queuesLen())