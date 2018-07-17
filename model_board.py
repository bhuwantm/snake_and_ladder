from const_values import snake_positions, ladder_positions, snake_foreground, snake_background, ladder_foreground, \
    ladder_background, winner_foreground, winner_background


class Tile:
    """  Represent tile in game """

    def __init__(self, value=None, x=None, y=None, foreground = "#333",background = "#fff"):
        self.value = value
        self.x = x
        self.y = y
        self.foreground = foreground
        self.background = background

class SnakeLadder():
    """ Represents either snake or a ladder """

    def __init__(self, type='S', initial_tile=None, final_tile=None):
        self.type = type
        self.initial_tile = initial_tile
        self.final_tile = final_tile


class Board:
    """ Represents Board containg all the elements """

    def __init__(self):
        self.tile_set = []
        self.snake_set = [SnakeLadder('S', x[0], x[1]) for x in snake_positions]
        self.ladder_set = [SnakeLadder('L', x[0], x[1]) for x in ladder_positions]

        # Generating tileset properties
        xcounter = 10
        ycounter = 0
        ymanipulator = 1

        for x in xrange(100):
            self.tile_set.append(Tile(x + 1, xcounter, ycounter))

            if x != 0 and (x + 1) % 10 == 0:
                xcounter -= 1
                ymanipulator *= -1
            else:
                ycounter = ycounter + ymanipulator


        # Changing color for snake ladder or normal tile
        snake_set_intials = [x.initial_tile for x in self.snake_set]
        ladder_set_initials = [x.initial_tile for x in self.ladder_set]

        for tile in self.tile_set:
            if tile.value in snake_set_intials:
                tile.foreground = snake_foreground
                tile.background = snake_background
            elif tile.value in ladder_set_initials:
                tile.foreground = ladder_foreground
                tile.background = ladder_background
            elif tile.value == 100:
                tile.foreground = winner_foreground
                tile.background = winner_background