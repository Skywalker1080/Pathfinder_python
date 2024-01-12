from pathfinding.core import grid
from pathfinding.finder.a_star import AStarFinder

matrix = [
    [1,1,1,1,1,1],
    [1,0,1,1,1,1],
    [1,1,1,1,1,1]
]
# Create a grid
Grid = grid(matrix = matrix)

# Create a start and end cell
start = Grid.node(0,0)
end = Grid.node(5,2)

# Create a finder
finder = AStarFinder()

# Use the finder
path,runs = finder.find_path(start,end,grid)

print(path)


def create_path(self):
    # Start
    start_x, start_y = [1, 1]
    start = self.grid.node(start_x, start_y)

    # End
    mouse_pos = pygame.mouse.get_pos()
    end_x = mouse_pos[0] // 32
    end_y = mouse_pos[1] // 32
    end = self.grid.node(end_x, end_y)

    finder = AStarFinder(diagonal_movement=DiagonalMovement.always)

    path = finder.find_path(start, end, self.grid)
    self.path = path
    self.grid.cleanup()