class Team: 

    def __init__(self, name, players, coach):
        self.players = players
        self.coach = coach 
        self.name = name
        self.points = 0
    
    def add_player(self, new_player_name):
        self.players.append(new_player_name)
    
    def has_player(self, find_players_name):
        return find_players_name in self.players
        
    def play_game(self, won):
        if won: 
            self.points += 3
