class Film():
    def __init__ (self, id, title, rating):
        self.id = id,
        self.title = title,
        self.rating = rating

class Actor():
    def __init__(self, id, name):
        self.id = id,
        self.name = name


class Imdb_graph():
    #Vi har kommet frem til at denne typer graf er en Bipartite graf
    #Der V kan representeres som en mengde V1 og V2, eller skuespillere og filmer
    #https://www.geeksforgeeks.org/dsa/bipartite-graphs-in-python/
    def __init__ (self):
        self.actors = set() #V1
        self.movies = set() #V2
        self.adj_list = {} #E

    def insert_film(self, film_parts):
        new_film = Film(film_parts[0], film_parts[1], film_parts[2])
        self.movies.add(new_film)

    def insert_actor(self, actor_parts):
        new_actor = Actor(actor_parts[0], actor_parts[1])
        self.actors.add(new_actor)

    def connect(self, connector):
        #connector består av [ttid, nmid]
        movie, actor = connector[0], connector[1]
        #if (u in self.U and v in self.V) or (u in self.V and v in self.U):
        self.adj_list.setdefault(movie, []).append(actor)
        self.adj_list.setdefault(actor, []).append(movie)

    def BFSFull(self):
        components = []
        visited = set()
        V = list(self.actors) + list(self.movies)
        for v in V:
            if v not in visited:
                number_of_actors = self.BFSVisit(self.adj_list, v, visited)
                components.append(number_of_actors)

        return components

    #Feil retur type i forhold til å finne korteste sti fra skuespiller1 til 2
    def BFSVisit(self, E, s, visited):
        counter = 0
        visited.add(s)
        queue = []
        queue.append(s)

        while queue: 
            u = queue.pop(0)
            for v in E[u]:
                if v not in visited:
                    visited.append(v)
                    queue.append(v)
                    if v.instanceOf(Actor):
                        counter += 1

        return counter

    def printComponents(self):
        components = self.BFSFull()

        antall = {}
        for tall in components:
            antall[tall] = components.get(tall, 0) + 1

        for tall, n in antall.items():
            print(f"There are {n} of size {tall}")
            
            


    """
    There are 1 components of size 1
    There are 1 components of size 3
    """

                        

        