import sys
from timeit import timeit
from generator.eulerian_generator import generateEulerianGraph
from algos.euler import euler
from algos.hamilton import hamilton

def main():
    if(len(sys.argv) <= 2):
        print("Nie podano wszystkich parametrów. Sposób wywołania:")
        print("zad1.py <nasycenie w %> <ilość wierzchołków>")
        exit(1)
    pass

    saturation = float(sys.argv[1])

    if saturation < 0 or saturation > 100:
        print("Nasycenie musi być z przedziału [0%, 100%]")
        print("Podano: ", saturation, "%", sep="")
        exit(1)
    saturation /= 100

    size = int(sys.argv[2])

    graph = generateEulerianGraph(size, saturation)

    (euler_time, hamilton_time) = measureTime(graph)

    print()
    print("      Elementów | ", str(size).rjust(10, " "), sep="")
    print("----------------+------------")
    print("    Algorytm    | Wynik (ms) ")
    print("----------------+------------")
    print("   Obwód Eulera | ", str(euler_time).rjust(10, " "), sep="")
    print(" Cykl Hamiltona | ", str(hamilton_time).rjust(10, " "), sep="")
    print()

def measureTime(graph):
    repetitions = 5

    print("Wyznaczanie obwodu Eulera...")
    euler_time = 0
    for i in range(repetitions):
        print("Przebieg #", i+1, ": ...", sep="")
        time = timeit(lambda: euler(graph), number=1)
        print("\033[1APrzebieg #", i+1, ": ", int(time * 1e3), " ms", sep="")
        euler_time += time / repetitions
    euler_time = int(euler_time * 1e4) / 10

    print("Wyznaczanie cyklu Hamiltona...")
    hamilton_time = 0
    for i in range(repetitions):
        print("Przebieg #", i+1, ": ...", sep="")
        time = timeit(lambda: hamilton(graph), number=1)
        print("\033[1APrzebieg #", i+1, ": ", int(time * 1e3), " ms", sep="")
        hamilton_time += time / repetitions
    hamilton_time = int(hamilton_time * 1e4) / 10

    return (euler_time, hamilton_time)

main()