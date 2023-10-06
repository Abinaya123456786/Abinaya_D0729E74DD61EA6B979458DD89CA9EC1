
#base class
class Player:
    def play(self):
        print("The player is playing Cricket.")

#derived class Batsman
class Batsman(Player):
    def play(self):
        print("The batsman is batting.")


#derived class Bowler
class Bowler(Player):
    def play(self):
        print("The bowler is bowling.")

#Creating objects
bman=Batsman()
bow=Bowler()
for p in (bman,bow):
    p.play()