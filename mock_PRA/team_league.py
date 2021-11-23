class Team:
    def __init__(self, owner, value, id1, name):
        self.owner = owner
        self.value = value
        self.id1 = id1
        self.name = name

class League:
    def __init__(self, team_list, league):
        self.league = league
        self.team_list = team_list

    def find_minimum_team_by_Id(self):
        minim = 999999
        obj = None
        for each in self.team_list:
            if each.id1 < minim:
                minim = each.id1
                obj = each
        return obj

    def sort_by_team_Id(self):
        l = []
        for each in self.team_list:
            l.append(each.id1)
        return sorted(l) if len(l)!=0 else None
n = int(input())
l = []
for i in range(n):
    own = input()
    value = float(input())
    id = int(input())
    name = input()
    l.append(Team(own,value,id,name))

obj = League(l,"league")
x = obj.find_minimum_team_by_Id()
y = obj.sort_by_team_Id()
if x == None:
    print("No Data Found")
else:
    print(x.owner)
    print(x.value)
    print(x.id1)
    print(x.name)
if y == None:
    print("No Data Found")
else:
    for i in y:
        print(i)
