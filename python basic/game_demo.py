class Game:
    top_score = 0

    def __init__(self, new_player_name):
        self.player_name = new_player_name

    @staticmethod
    def show_help():
        print("Game help.........")

    @classmethod
    def show_top_score(cls):
        print("Top score is %d" % Game.top_score)

    def start_game(self):
        print("%s is starting to play game..." % self.player_name)

    def __new__(cls, *args, **kwargs):
        print("...")

Game.top_score = 99
gamer1 = Game("Peter")
gamer1.start_game()
gamer1.show_help()
gamer1.show_top_score()
