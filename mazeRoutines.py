import cell

def index(data, x, y):
    if x < 0 or y < 0 or x > (len(data) ** 0.5) - 1 or y > (len(data) ** 0.5) - 1:
        return -1
    return int(x + y * (len(data) ** 0.5))

def getXY(data, index):
	l = len(data) ** 0.5
	x = int(index // l)
	y = int(index % l)
	return x, y

def getNeighbours(current, cells):
		possibles = []

		current = cell.Cell(current[0], current[1])

		n = index(cells, current.x, current.y+1)
		e = index(cells, current.x+1, current.y)
		s = index(cells, current.x, current.y-1)
		w = index(cells, current.x-1, current.y)

		if n != -1:
			possibles.append(n)
		if e != -1:
			possibles.append(e)
		if s != -1:
			possibles.append(s)
		if w != -1:
			possibles.append(w)

		return [getXY(cells, p) for p in possibles]

def h(n, goal):
	""" Estimates the cost to reach a goal node from node n using Pythagoras' Theorem.
	Used as the heuristic in the below A* algorithm.
	'n' and 'goal' are tuples of co-ordinates (x,y). """

	b = abs(n[0] - goal[0])
	c = abs(n[1] - goal[1])

	a = ((b ** 2) + (c ** 2)) ** 0.5   ## Pythagoras
	return a


def reconstructPath(cameFrom, current):
	return cameFrom

def aStar(maze, start, goal):
	""" Returns a list of directions to get from 'start' to 'end'.
	'start' and 'goal' are tuples of co-ordinates (x,y). """

	openSet = [start]
	cameFrom = [0 for x in range(len(maze))]

	fScore = [0 for x in range(len(maze))]
	gScore = [99999999 for x in range(len(maze))]

	fScore[index(maze, start[0], start[1])] = h(start, goal)
	gScore[index(maze, start[0], start[1])] = 0

	while openSet:
		current = openSet[fScore.index(min(fScore))]
		if current == goal:
			return reconstructPath(cameFrom, current)

		openSet.remove(current)
		neighbours = getNeighbours(current, maze)
		for neighbour in neighbours:
			tentativeG = gScore[index(maze, current[0], current[1])] + 1
			mazeIndex = index(maze, neighbour[0], neighbour[1])
			if tentativeG < gScore[mazeIndex]:
				cameFrom[mazeIndex] = current
				gScore[mazeIndex] = gScore[index(maze, current[0], current[1])]
				fScore[mazeIndex] = gScore[mazeIndex] + h(getXY(maze, mazeIndex), goal)
				if neighbour not in openSet:
					openSet.append(neighbour)

	return "Fail"
				


