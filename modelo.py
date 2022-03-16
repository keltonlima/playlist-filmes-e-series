from ast import List


class Programa():
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0
        
    @property
    def likes(self):
        return self._likes
        
    def dar_likes(self):
        self._likes += 1
            
    @property
    def nome(self):
        return self._nome
        
    @nome.setter
    def nome(self, nome):
        self._nome = nome
        
    def __str__(self):
        return f'{self._nome}, {self.ano}'


class Filmes(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao
        
    def __str__(self):
        return f'{self._nome}, {self.duracao}, {self.ano}'

        
class Series(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas
        
    def __str__(self):
        return f'{self._nome}, {self.temporadas}, {self.ano}'  
    
    
class Playlist():
    def __init__(self, nome, programas):
        self.nome = nome
        self.programas = programas
        
    def __getitem__(self, item):
        return self.programas[item]
        
    @property
    def listagem(self):
        return self.programas
    
    def __len__(self):
        return len(self.programas)

        
vingadores = Filmes("Vingadores - Guerra Infinita", 2018, 180)
atlanta = Series("Atlanta", 2018, 2)
pantera = Filmes("Pantera Negra", 2018, 120)
himym = Series("How i met your mother", 2005, 9)


filmes_e_series = [vingadores, atlanta, pantera, himym]
playlist_fim_de_semana = Playlist('fim de semana', filmes_e_series)

for programa in playlist_fim_de_semana.listagem:
    print(programa)
    
print(f'Tamanho total da lista', len(playlist_fim_de_semana))