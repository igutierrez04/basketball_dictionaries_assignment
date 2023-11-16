class Player:
    def __init__(self, data):
        self.name = data['name']
        self.age = data['age']
        self.position = data['position']
        self.team = data['team']


    # returns a single player instance
    def player(self):
        print(f"Player: {self.name}, Age: {self.age}, Position: {self.position}, Team: {self.team}")
        return self


    # @classmethod
    # def get_team(cls, team_list):
    #     teams = []
    #     for i in team_list:
    #         teams.append(cls(i))
    #         return teams

    @classmethod
    def add_players(cls, data):
        player_objects = []
        for dict in data:
            player_objects.append(cls(dict))
        return player_objects


kevin = {
    "name": "Kevin Durant",
    "age": 34,
    "position": "small forward",
    "team": "Brooklyn Nets"
}

jason = {
    "name": "Jason Tatum",
    "age": 24,
    "position": "small forward",
    "team": "Boston Celtics"
}

kyrie = {
        "name": "Lyrie Irving",
    "age": 32,
    "position": "point guard",
    "team": "Brooklyn Nets"
}

player_kevin = Player(kevin) 
player_jason = Player(jason)
player_kyrie = Player(kyrie)
print(player_kevin) # returns player location in memory
print(player_jason) # returns player location in memory
print(player_kyrie) # returns player location in memory

player_jason.player()
player_kevin.player()
player_kyrie.player()

players = [
    {
        "name": "Kevin Durant",
        "age": 34,
        "position": "small forward",
        "team": "Brooklyn Nets"
    },
    {
        "name": "Jason Tatum",
        "age": 24,
        "position": "small forward",
        "team": "Boston Celtics"
    },
    {
            "name": "Lyrie Irving",
        "age": 32,
        "position": "point guard",
        "team": "Brooklyn Nets"
    },
    {
        "name": "Damian Lillard",
        "age": 33,
        "position": "Point Guard",
        "team": "Portland Trailblazers"
    },
    {
        "name": "Joel Embiid",
        "age": 32,
        "position": "Power Foward",
        "team": "Philadelphia 76ers"
    }
]
# new_team = []
# for player_dict in player_list:
#     player = Player(player_dict)
#     new_team.append(player)

# print(new_team)

# player.get_team(new_team)

new_team = []

# for loop to add each player dictionary
for player_dict in players:
    player = Player(player_dict)
    new_team.append(player)

print(new_team)

new_players = Player.add_players(players)

print(new_players)
