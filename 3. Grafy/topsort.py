import sys
import timeit
from generator.dag_generator import generateDag
from representations.list_graph import ListGraph
from representations.matrix_graph import MatrixGraph
from sort.topological_list import topologicalSortList
from sort.topological_matrix import topologicalSortMatrix

def main():
    if len(sys.argv) <= 2:
        print("Nie podano wymaganych argumentów. Sposób wywołania:")
        print("topsort.py <nasycenie w %> <ilość wierzchołków>")
        exit(1)
    saturation = float(sys.argv[1]) / 100
    size = int(sys.argv[2])

    print("Generowanie grafu...")
    graph = generateDag(size, saturation)
    times = measureTime(graph)

    print()
    print("          Elementów | ", str(size).rjust(10, " "), sep="")
    print("--------------------+------------")
    print("    Reprezentacja   | Wynik (ms) ")
    print("--------------------+------------")
    print("  Lista następników | ", str(times[0]).rjust(10, " "), sep="")
    print(" Macierz sąsiedztwa | ", str(times[1]).rjust(10, " "), sep="")
    print()

def measureTime(src_graph):
    repetitions = 5
    list_graph = ListGraph(src_graph)
    matrix_graph = MatrixGraph(src_graph)

    print("Pomiar czasu dla reprezentacji listowej...")
    time = 0
    for i in range(repetitions):
        print("Rozpoczęto przebieg #", i+1, sep="")
        time += timeit.timeit(lambda: topologicalSortList(list_graph), number=1)
    avg_time_list = int(1e4 * time / repetitions) / 10
    
    print("Pomiar czasu dla reprezentacji macierzowej...")
    time = 0
    for i in range(repetitions):
        print("Rozpoczęto przebieg #", i+1, sep="")
        time += timeit.timeit(lambda: topologicalSortMatrix(matrix_graph), number=1)
    avg_time_matrix = int(1e4 * time / repetitions) / 10

    return (avg_time_list, avg_time_matrix)

main()