from random import randint

class location():

    def __init__(self):
        self.height = randint(0, 100)
        self.terrain = "water"
        self.strife = False
        self.population = 0

    # terrain_list = ['water', 'grassland', 'forrest', 'dessert', 'tundra']

    # def neighbor_adjust(self):


def world_build():

    grid = []
    size = int(input('Grid Size?: '))
    for i in range(size):
        x = []
        grid.append(x)
        for j in range(size):
            grid[i].append(location())
    return grid


def display_world(grid):
    for i in range(len(grid)):
        for j in range(len(grid)):
            print(grid[i][j].height, end=" ")
        print('\n')



def main():

    world = world_build()
    display_world(world)


if __name__ == main():
    main()