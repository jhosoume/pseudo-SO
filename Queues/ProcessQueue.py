from collections import deque
from ProcessManager.Process import Process

#Modulo responsavel por gerenciar as filas dos processos
class ProcessQueue():
	def __init__(self):
		self.queue = [deque(), deque(), deque(), deque()]

	def totalIn(self):
		return NotImplemented

	#Retorna o tamanho total das filas
	def queuesLen(self):
		return len(self.queue[0]) + len(self.queue[1]) + len(self.queue[2]) + len(self.queue[3])

	#Adiciona um processo novo a fila correspondente
	def addProcess(self, process):
		queues_size = self.queuesLen()
		if queues_size < 1000:
			self.queue[process.priority].append(process)
		else:
			print("Excedeu tamanho limite das filas")

	#Adiciona um processo que foi preemptado novamente a fila, diminuindo sua prioridade
	def readdProcess(self, process):
		if process.priority < 3:
			process.priority = process.priority + 1
		self.addProcess(process)

	#Pega o processo que esta em primeiro lugar da fila
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

	#Lista a fila de processos em ordem de prioridade
	def listInOrder(self):
		return list(self.queue[0]) + list(self.queue[1]) + list(self.queue[2]) + list(self.queue[3])

	#Remove um processo da fila
	def remove(self, process):
		for queue in range(4):
			if process in self.queue[queue]:
				self.queue[queue].remove(process)
	#Imprime o tamanho das filas
	def printQueues(self):
		print("Tamanho da fila 0:", len(self.queue[0]))
		print("Tamanho da fila 1:", len(self.queue[1]))
		print("Tamanho da fila 2:", len(self.queue[2]))
		print("Tamanho da fila 3:", len(self.queue[3]))
		print("Tamanho total das filas:", self.queuesLen())
