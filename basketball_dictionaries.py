class Player:
    def __init__(self, data):
        self.name = data['name']
        self.age = data['age']
        self.position = data['position']
        self.team = data['team']

    @classmethod
    def create_player(cls, data):
        pass












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
print(player_kevin)