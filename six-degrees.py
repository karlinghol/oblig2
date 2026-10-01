import sys
from imdb_graph import Imdb_graph

def debug(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

def main():
    debug("Dette er et eksempel på å printe debug info. Du kan slette denne linjen")

    imdb_graph = Imdb_graph()

    M = int(input())
    for i in range(M):
        parts = input().split("\t");
        imdb_graph.insert_film(parts)
        # parts består av [ttid, tittel, rating]

    A = int(input())
    for i in range(A):
        parts = input().split("\t");
        imdb_graph.insert_actor(parts)
        # parts består av [id, navn]

    E = int(input())
    for i in range(E):
        parts = input().split("\t");
        imdb_graph.connect(parts)
        # parts består av [ttid, nmid]

    # Finn komponenter
    imdb_graph.printComponents()

    Qs = int(input())
    for i in range(Qs):
        parts = input().split("\t");
        print(imdb_graph.find_shortest_path(parts))
        # parts består av [nmid₁, nmid₂]

        # Finn korteste vei og print ut på en linje

    Qc = int(input())
    for i in range(Qc):
        parts = input().split("\t");
        # parts består av [nmid₁, nmid₂]

        # Finn chilleste vei og print ut på en linje

main()
