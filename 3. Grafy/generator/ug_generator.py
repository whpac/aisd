from random import random
from generator.pseudorandom import psrandomOneToThousand
from generator.graph_node import GraphNode

# Generuje graf nieskierowany o nodes_count wierzchołkach
# Nasycenie krawędziami będzie wynosiło w przybliżeniu saturation
# Parametr saturation musi być z przedziału [0, 1].
def generateUg(nodes_count: int, saturation: float) -> list:
    saturation = 0 if saturation < 0 else saturation
    saturation = 1 if saturation > 1 else saturation

    graph = createEmptyGraph(nodes_count)
    connectVertices(graph, saturation)
    connectSubgraphs(graph)
    return graph

# Tworzy graf bez łuków
def createEmptyGraph(nodes_count: int) -> list:
    graph = []

    for i in range(nodes_count):
        node = GraphNode()
        node.id = i
        node.isAttached = False
        graph.append(node)

    return graph

# Tworzy połączenia (powstały graf może być niespójny)
def connectVertices(graph: list, probability: float) -> None:
    for i in range(len(graph)):
        for j in range(i + 1, len(graph)):
            if probability <= random():
                continue
            weight = psrandomOneToThousand()
            graph[i].addSuccessor(graph[j], weight)
            graph[j].addSuccessor(graph[i], weight)

# Łączy podgrafy, by stworzyć graf spójny
def connectSubgraphs(graph: list) -> None:
    for i in range(len(graph)):
        node = graph[i]
        if node.isAttached:
            continue
        if i > 0:
            weight = psrandomOneToThousand()
            graph[i-1].addSuccessor(node, weight)
            node.addSuccessor(graph[i-1], weight)
        markAsAttached(node)

# Oznacza podgraf jako dołączony do grafu wynikowego
def markAsAttached(node: GraphNode) -> None:
    nodes_to_mark = [node]

    while len(nodes_to_mark) > 0:
        node = nodes_to_mark.pop()
        if node.isAttached:
            continue

        node.isAttached = True
        for child, _weight in node.successors:
            nodes_to_mark.append(child)
