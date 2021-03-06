from collections import deque
from algos.bst import BSTree

def prim(graph, count_wrapper = [0]):
    edges = deque()
    for i in range(graph.getVertexCount()):
        for succ, weight in graph.getImmediateSuccessors(i):
            if i < succ:
                edges.append((i, succ, weight))

    edges = sorted(edges, key=lambda x: x[2])
    visited = BSTree()
    out_edges = deque()
    to_visit = graph.getVertexCount() - 1

    visited.addNode(int(to_visit / 2))

    cnt = 0

    while to_visit > 0:
        for edge in edges:
            cnt += 1
            start_in = visited.find(edge[0])
            end_in = visited.find(edge[1])

            if start_in and not end_in:
                out_edges.append(edge)
                visited.addNode(edge[1])
                to_visit -= 1
                break

            if not start_in and end_in:
                out_edges.append(edge)
                visited.addNode(edge[0])
                to_visit -= 1
                break
        else:
            break

    count_wrapper[0] = cnt

    if to_visit > 0:
        return None
    return out_edges
