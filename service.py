from const_values import tile_height, tile_width, player_height, player_width


def player_posx_br(init_x):
    """ Provides xcoordinate for positioning player inside tile at bottom right """
    return init_x + tile_width - player_width


def player_posy_br(init_y):
    """ Provides ycoordinate for positioning player inside tile at bottom right """
    return init_y + tile_height - player_height



def player_posx_center(init_x):
    """ Provides xcoordinate for positioning player inside tile at center """
    return init_x + (tile_width/2) -  (player_width / 2)


def player_posy_center(init_y):
    """ Provides ycoordinate for positioning player inside tile at center """
    return init_y + (tile_height/2) -  (player_height / 2)



