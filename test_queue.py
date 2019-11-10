from Queues.ProcessQueue import *


processes = [Process([0, 1, 1, 1, 1, 0, 0, 2]),
             Process([0, 3, 1, 1, 2, 1, 1, 1]),
             Process([0, 1, 1, 1, 1, 0, 0, 0]),
             Process([0, 0, 1, 1, 1, 0, 0, 2]),
             Process([0, 0, 1, 1, 1, 0, 0, 2])]
pid = 0
for proc in processes:
    proc.pid = pid
    pid += 1

pq = ProcessQueue()
for proc in processes:
    pq.addProcess(proc)

for proc in pq.listInOrder():
    print(proc.pid)
