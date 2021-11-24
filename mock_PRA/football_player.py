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
        return max(self.pl,key = lambda x:x.r) if len(self.pl)!=0 else None
    def sortbygoals(self):
        return sorted(self.pl , key = lambda x:x.g) if len(self.pl) !=0 else None
            
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
        
        
        """
        
        70
88
9
Cristiano Ronaldo
24
31
62
87
88
        
        70
88
9
Cristiano Ronaldo
24
31
62
87
88
        
        """