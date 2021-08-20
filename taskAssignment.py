def taskAssignment(k, tasks):
	tasks = [(i, tasks[i]) for i in range(len(tasks))]
	tasks = sorted(tasks, key=lambda task: task[1])
	optimal = []
	for i in range(len(tasks) // 2):
		optimal.append([tasks[i][0], tasks[len(tasks) - 1 - i][0]])
	return optimal