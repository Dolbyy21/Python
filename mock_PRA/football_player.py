# football-player
class Player:
    def __init__(self, matches, goals, rating, name):
        self.m = matches
        self.g = goals
        self.r = rating
        self.n = name
class FootballLeague:
    def __init__(self,league_name, player_list):
        self.ln = league_name
        self.pl = player_list   
    def findmax(self):
        if len(self.pl) == 0:
            return None
        maxm = -1
        obj = None
        for i in self.pl:
            if i.r > maxm:
                maxm = i.r
                obj = i
        return obj 
    def sortbygoals(self):
        l = []
        for i in self.pl:
            l.append(i.g)
        if len(self.pl) == 0:
            return None
        return sorted(l)
            
n = int(input())
l = [] 
for i in range(n):
    ma = int(input())
    g = int(input())
    r = int(input())
    n = input()
    l.append(Player(ma,g,r,n))
obj = FootballLeague(" ", l)
x = obj.findmax()
if x == None:
    print("No Data Found") 
else:
    print(x.m)
    print(x.g)
    print(x.r)
    print(x.n)
y = obj.sortbygoals()
if y == None:
    print("No Data Found")
else:
    for i in y:
        print(i.g)

