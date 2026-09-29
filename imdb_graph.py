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
    def __init__ (self):
        self.graph = {}
        self.actors = {}

    def insert_film(self, film_parts):
        new_film = Film(film_parts[0], film_parts[1], film_parts[2])
        self.graph.update({new_film: set()})

    def insert_actor(self, actor_parts):
        self.actors.update({actor_parts[0], actor_parts[1]})

    def connect(self, connector):
        film_id, actor_id = connector[0], connector[1]
        actor = Actor(actor_id, self.actors[actor_id])
        self.graph[film_id].add(actor)


    def full_dfs(self):
        visted = []
        for movie in self.graph:
            if movie not in visted:
                dfs(self.graph, movie, visited)

    def dfs(graph, movie, visited):
        #Vi skal sette alle skuespillerne som er i filmen i en stack og i visited
        #Så sjekker vi om skuespillern (neste fra stacken) har overlapp med en annen ny film 
        #Hvis ja, legger vi den filmen i stacken og i visited
        #Hvis nei, sjekker vi neste element i stacken
        pass
        
