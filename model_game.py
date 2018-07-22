import random
from itertools import chain

from model_board import Board


class Dice():
    """ Represents game dice """

    def __init__(self, no_of_faces):
        self.faceValues = [x + 1 for x in xrange(no_of_faces)]
        self.current_face = None

    def roll_dice(self):
        """ Roll the dice to change current-face value """
        self.current_face = self.faceValues[random.randint(0, len(self.faceValues) - 1)]


class Player:
    """ Represents individual player """

    def __init__(self, name,background="607D8B",foreground="#fff"):
        self.name = name
        self.current_tile = 0
        self.foreground = foreground
        self.background = background


    def reset_position(self):
        """ Resets position of player if eaten by other player """
        self.current_tile = 0


class Game:
    """ Represents all the element of snakes and ladder game """

    def __init__(self):
        self.board = Board()
        self.dice = Dice(6)
        self.player_list = []
        self.cpi = None #Current player index

    def init_player(self, *args):
        """ Initializer players by their name """

        self.player_list = [Player(x[0],x[1]) for x in args]
        self.cpi = 0



    def _update_players_tile(self):
        """ updates tile for each player to next state """

        if self.player_list[self.cpi].current_tile != 0:
            """ If player is already in tile of the board """
            self.player_list[self.cpi].current_tile += self.dice.current_face
        elif self.dice.current_face == 1:
            """ Put player to board only if face value is 1 """
            self.player_list[self.cpi].current_tile += self.dice.current_face

        cp_tile = self.player_list[self.cpi].current_tile

        if cp_tile > len(self.board.tile_set):
            """ Reverse movement if current player tile excides max tile_set length """
            self.player_list[self.cpi].current_tile = 100 - (cp_tile - 100)


        for sl in chain(self.board.snake_set,self.board.ladder_set):
            """ Update player position if player tile lands on inital_position of sanke or ladder """

            if self.player_list[self.cpi].current_tile == sl.initial_tile:
                self.player_list[self.cpi].current_tile = sl.final_tile


        for index, player in enumerate(self.player_list):
            """ Represents a player consuming another player """
            if index == self.cpi:
                pass
            else:
                if self.player_list[self.cpi].current_tile == player.current_tile:
                    player.reset_position()



    def _update_cpi(self):
        """ Updates current player index i.e. player change """
        if not self.dice.current_face in [1,len(self.dice.faceValues)]:
            self.cpi = 0 if self.cpi + 1 >= len(self.player_list) else self.cpi + 1


    def _update_game_state(self):
        """ Updates current game state like players position, winner etc """

        self._update_players_tile()
        self._update_cpi()


    def roll_dice(self):
        """ Represents action of rolling the dice """

        self.dice.roll_dice()
        self._update_game_state()