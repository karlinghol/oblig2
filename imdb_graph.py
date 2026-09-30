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
    def __init__ (self):
        #Vi representerer grafen som en naboliste
        #Den er implementert som en ordbok
        #Der en en V er nøkkel og en mengde med u er dens verdi
        self.G = {}

    def insert_film(self, film_parts):
        new_film = Film(film_parts[0], film_parts[1], film_parts[2])
        self.G[new_film] = set()
    
    def insert_actor(self, actor_parts):
        new_actor = Actor(actor_parts[0], actor_parts[1])
        self.G[new_actor] = set()

    def connect(self, connector):
        #connector består av [ttid, nmid]
        #Vi tar utgangspunkt i her, at vi kunn kobler sammen skuespillere og filmer som allerede er lagt inn
        movie, actor = connector[0], connector[1]
        self.G[movie].add(actor)
        self.G[actor].add(movie)

    def CountComponents(self):
        #Dette representerer en liste av komponenter
        #Hver index represneterer en komponentent, og verdien er størrelsen på komponenten
        components_size = []
        visited = set()
        for v in self.G:
            if v not in visited:
                components_size.append(self.DFSVisit(self.G, v, visited))

        return components_size

    #Det er lurt å gjøre denne metoden iterativ, siden vi skal returnere
    #størrelsen på hver komponent
    def DFSVisit(G, s, visited):
        #Vi er bare ute etter å vite hvor mange skuespillere som er i komponenten
        amount_of_actors = 0
        stack = [s]
        while stack:
            u = stack.pop()
            if isinstance(u, Actor):
                amount_of_actors += 1
            
            if u not in visited:
                stack.add(u)
                #Pseudokoden er egentlig ute etter å 
                #finne hver kant i grafen som starter i u
                for v in G[u]:
                    #Samme som .push(v)
                    stack.append(v)
        
        return amount_of_actors


    def printComponents(self):
        components = self.CountComponents()

        antall = {}
        for tall in components:
            antall[tall] = components.get(tall, 0) + 1

        for tall, n in antall.items():
            print(f"There are {n} of size {tall}")

    #Midlertidig
    def find_shortest_path(graph, start, end, path =[]):
        path = path + [start]
        if start == end:
            return path
        shortest = None
        for node in graph[start]:
            if node not in path:
                newpath = find_shortest_path(graph, node, end, path)
                if newpath:
                    if not shortest or len(newpath) < len(shortest):
                        shortest = newpath
        return shortest
            


    """
    There are 1 components of size 1
    There are 1 components of size 3
    """

                        

        