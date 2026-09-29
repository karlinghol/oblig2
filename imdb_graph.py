class Film():
    def __init__ (self, id, title, rating):
        self.id = id,
        self.title = title,
        self.rating = rating

    #Siden vi ønsker å lagre hele film objekter som nøkler i nabolisten
    #Er vi avhengig og kunne slå opp på id for å kunne finne tilbake til Film objektet
    #Vi implementerer derfor __hash__ og __eq__ 
    def __hash__(self):
        return hash(self.id)

    def __eq__(self, other):
        if isinstance(other, Film):
            self.rating = Film.rating
        #Dette sørger for at vi sammenligner på id, selv om det vi sjekker er ett Film objekt eller en string med id
        if isinstance(other, str):
            return self.id == other

class Actor():
    def __init__(self, id, name):
        self.id = id,
        self.name = name


class imdb_graph():
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
        new_actor = Actor({actor_parts[0], actor_parts[1]})

    def connect(self, connector):
        #connector består av [ttid, nmid]
        movie, actor = connector[0], connector[1]
        #if (u in self.U and v in self.V) or (u in self.V and v in self.U):
        self.adj_list[movie].append(actor)
        self.adj_list[actor].append(movie)

    def BFSFull(self):
        visited = set()
        V = list(self.actors) + list(self.movies)
        for v in V:
            if v not in visited:
                BFSVisit(self.adj_list, v, visited)

    def BFSVisit(self, E, s, visited):
        visited.add(s)
        queue = []
        queue.append(s)

        while queue != []: 
            u = queue.pop(0)
            for (u, v) in E:
                if v not in visited:
                    visited.append(v)
                    queue.append(v)

        