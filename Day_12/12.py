from collections import defaultdict


def makeGraph(lines : list) -> list:
    graph = defaultdict(list)

    for line in lines:
        a, b = line.split("-")
        graph[a].append(b)
        graph[b].append(a)

    return graph

def isCap(text : str) -> bool:
    return text != text.lower()


def processNode(graph : defaultdict, node : str, prevNodes = [], before = False ,small_cave = None ) -> list: 
    paths = []
    prevNodes.append(node)


    for point in graph[node]:
        if point == "end":
            paths.append(["end"])
        elif point == "start":
            pass
        elif isCap(point):
            paths += processNode(graph, point, prevNodes.copy(), before, small_cave)    
        else: 
            if point in prevNodes:
                if before and small_cave == None: 
                    paths += processNode(graph, point, prevNodes.copy(), before, point)
            else:
                paths += processNode(graph, point, prevNodes.copy(), before, small_cave)
    temp = []
    for path in paths:
        temp.append([node]+path)
    return temp
        



with open("input.txt", "r") as f:
    lines = [line.strip("\n") for line in f.readlines()]

graph = makeGraph(lines)
print(graph)
paths = (processNode(graph, "start"))
print(len(paths))
    

paths = (processNode(graph, "start" , before = True))
print(len(paths))
    