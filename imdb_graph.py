from collections import deque

class Film():
    def __init__ (self, id, title, rating):
        self.id = id
        self.title = title
        self.rating = rating

class Actor():
    def __init__(self, id, name):
        self.id = id
        self.name = name

class Imdb_graph():
    def __init__ (self):
        #Vi representerer grafen som en naboliste
        #Den er implementert som en ordbok
        #Der en en V er nøkkel og en mengde med u er dens verdi
        self.G = {}
        self.objects = {}   # id -> Film/Actor-objekt

    def insert_film(self, film_parts):
        new_film = Film(film_parts[0], film_parts[1], film_parts[2])
        self.G[new_film] = set()
        self.objects[new_film.id] = new_film
    
    def insert_actor(self, actor_parts):
        new_actor = Actor(actor_parts[0], actor_parts[1])
        self.G[new_actor] = set()
        self.objects[new_actor.id] = new_actor

    def connect(self, connector):
        #connector består av [ttid, nmid]
        #Vi tar utgangspunkt i her, at vi kunn kobler sammen skuespillere og filmer som allerede er lagt inn
        movie = self.objects[connector[0]]
        actor = self.objects[connector[1]]
        self.G[movie].add(actor)
        self.G[actor].add(movie)

    def find_shortest_path(self, start_end):
        start_actor = self.objects[start_end[0]]
        end_actor = self.objects[start_end[1]]

        queue = deque()
        queue.append(start_actor)
        """
        Det vi bygger her en oversikt over nodenes foreldre. Så kan vi gå baklengs fra siste node til start noden
        Så {
        A : None
        B : A
        C : A
        D : C
        }
        """
        parents = {start_actor: None}

        while queue:
            current = queue.popleft() #Kaller den current, for å skjønne det bedre

            for neighbor in self.G[current]:
                if neighbor not in parents:
                    parents[neighbor] = current
                    
                    if neighbor == end_actor:
                        return self.format_path(parents, end_actor)
                    
                    queue.append(neighbor)

    def format_path(self, parents, end_node):
        path = []
        node = end_node
        while node is not None:
            path.append(node)
            node = parents[node]
        
        return "\t".join(v.id for v in reversed(path))
        
    def countComponents(self):
        #Dette representerer en liste av komponenter
        #Hver index represneterer en komponentent, og verdien er størrelsen på komponenten
        components = []
        visited = set()
        for v in self.G:
            if v not in visited:
                components.append(self.DFSVisit(v, visited))

        return components

    #Det er lurt å gjøre denne metoden iterativ, siden vi skal returnere
    #størrelsen på hver komponent
    def DFSVisit(self, s, visited):
        #Vi er bare ute etter å vite hvor mange skuespillere som er i komponenten
        amount_of_actors = 0
        stack = [s]
        while stack:
            u = stack.pop()
            if u not in visited:
                visited.add(u)
                if isinstance(u, Actor):
                    amount_of_actors += 1
                for v in self.G[u]: #Pseudokoden er egentlig ute etter å finne hver kant i grafen som starter i u
                    stack.append(v)
        
        return amount_of_actors

    def printComponents(self):
        components = self.countComponents()

        #Et tall som svarer til antall forskjellige komponentstørrelser.
        print(len(set(components)))

        counts = {}

        for component in components:
            if component in counts:
                counts[component] += 1
            else:
                counts[component] = 1
        for number, n in counts.items():
            print(f"There are {n} of size {number}")

        