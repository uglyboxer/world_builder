from random import choice, randint, randrange

class room:

    def __init__(self, possible_exits):

        self.possible_exits = possible_exits
        self.exits = randint(1, len(self.possible_exits))
        self.actual_exits = [self.possible_exits.pop(self.possible_exits.index(choice(self.possible_exits)))
                             for i in range(self.exits)] #need to pop from list

        #Adversaries
        #Items (and their location, called from another class)
        #Depth in dungeon
        #"Layer" in story (which of the Five Room Dungeon, is this?)



# Perhaps these end up in different modules?

class item:

    def __init__(self):
        #item_name
        #place in the room
        #moveble?
        pass

class npc:

    def __init__(self):
        #species
        #gender
        #size
        #speed
        #weapon
        #defense
        #attack
        #things it may say
        pass


def check_neighbors(dungeon, dungeon_room, entered_from):

    possible_exits = ['u', 'd', 'w']

    return possible_exits



def print_dungeon(level, dungeon):
       for i in range(20):
        for j in range(20):
            print(dungeon[level][i][j], " ", end="")
        print("\n")



# Create a list of lists for dungeon with 0 placeholders to start.
# Random start of dungeon (the descent) and develop as it goes.  Check surrounding 10 neighbors, and ignore if 0
# Act accordingly in designing the room if neighbor exists and doors or walls line up

def main():
    dungeon = [[[0 if (
        (i != 0) and
        (i != 19) and
        (j != 0) and
        (j != 19))
        else 1 for i in range(20)] for j in range(20)] for k in range(3)]

    start_location = randint(1, 18), randint(1,18)
    possible_exits = ['u', 'd', 'w', 'e', 'n']
    dungeon[0][start_location[1]][start_location[0]] = room(possible_exits)
    # print(dungeon[0][start_location[1]][start_location[0]].actual_exits)
    # ('n', 'ne', 'e', 'se', 's', 'sw', 'w', 'nw', 'u', 'd')
    print_dungeon(0, dungeon)



main()
