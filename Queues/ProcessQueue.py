from collections import deque
from ProcessManager.Process import Process

class ProcessQueue():
	def __init__(self):
		self.queue = [deque(), deque(), deque(), deque()]

	def totalIn(self):
		return NotImplemented

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

	def getProcess(self):
		if len(self.queue[0]) > 0:
			return self.queue[0].popleft()
		elif len(self.queue[1]) > 0:
			return self.queue[1].popleft()
		elif len(self.queue[2]) > 0:
			return self.queue[2].popleft()
		elif len(self.queue[3]) > 0:
			return self.queue[3].popleft()
		else:
			print("Nenhum processo na fila")
			return Process()

	def listInOrder(self):
		return list(self.queue[0]) + list(self.queue[1]) + list(self.queue[2]) + list(self.queue[3])

	def remove(self, process):
		for queue in range(4):
			if process in self.queue[queue]:
				self.queue[queue].remove(process)

	def printQueues(self):
		print("Tamanho da fila 0:", len(self.queue[0]))
		print("Tamanho da fila 1:", len(self.queue[1]))
		print("Tamanho da fila 2:", len(self.queue[2]))
		print("Tamanho da fila 3:", len(self.queue[3]))
		print("Tamanho total das filas:", self.queuesLen())
