from PyQt4 import QtGui
from PyQt4 import QtCore

from const_values import tile_height, tile_width, player_height, player_width, player_radius, dice_face_simulation
from model_game import Game
from service import player_posx_br, player_posy_br


class GameWindow(QtGui.QMainWindow):
    def __init__(self):
        super(GameWindow, self).__init__()
        self.setWindowTitle("Snakes & Ladder")
        self.setWindowIcon(QtGui.QIcon('resources/favicon.ico'))
        self.setGeometry(300, 100, 750, 600)

        self.game_widget = GameWidget(self)
        self.setCentralWidget(self.game_widget)
        self.setStyleSheet("QMainWindow {background-color: #fff}")
        self.show()


class GameWidget(QtGui.QWidget):
    def __init__(self,parent):
        super(GameWidget, self).__init__(parent)
        self.player_widget_list = []
        self.player_widget_init_position = []
        self.tile_widget_list = []
        self.init_game()
        self.init_ui()

    def init_game(self):
        self.game = Game()
        self.game.init_player(["Player1","#607D8B"], ["Player2","#795548"], ["Player3","#5E35B1"])

    # def generate_board_grid(self):
    #     """ Generates grid to represent board """
    #
    #     grd = QtGui.QGridLayout()
    #     grd.setHorizontalSpacing(2)
    #     grd.setVerticalSpacing(2)
    #     for tile in self.game.board.tile_set:
    #         inner_grd = QtGui.QGridLayout()
    #         lbl_tile = QtGui.QLabel()
    #         lbl_tile.setText(str(tile.value))
    #         lbl_tile.setFixedHeight(tile_height)
    #         lbl_tile.setFixedWidth(tile_width)
    #         lbl_tile.setAlignment(QtCore.Qt.AlignCenter)
    #         lbl_tile.setStyleSheet(
    #             "QLabel{{ background-color : {}; color : {}; border: 1px solid #ccc; font-weight: bold;}}"
    #                 .format(tile.background, tile.foreground)
    #         )
    #         inner_grd.addWidget(lbl_tile)
    #         grd.addLayout(inner_grd,tile.x, tile.y)
    #     return grd

    def generate_board_grid(self):
        """ Generates grid to represent board """

        grd = QtGui.QGridLayout()
        grd.setHorizontalSpacing(0)
        grd.setVerticalSpacing(0)
        for tile in self.game.board.tile_set:
            lbl_tile = QtGui.QLabel()
            lbl_tile.setText(str(tile.value))
            lbl_tile.setFixedHeight(tile_height)
            lbl_tile.setFixedWidth(tile_width)
            lbl_tile.setAlignment(QtCore.Qt.AlignCenter)
            lbl_tile.setStyleSheet(
                "QLabel{{ background-color : {}; color : {}; border: 1px solid #ccc; font-weight: bold;}}"
                    .format(tile.background, tile.foreground)
            )
            self.tile_widget_list.append(lbl_tile)
            grd.addWidget(lbl_tile,tile.x, tile.y)
        return grd


    def generate_player_grid(self):
        """ Generates grid to place players """


        box = QtGui.QHBoxLayout()
        box.setContentsMargins(0,10,0,0)
        box.setAlignment(QtCore.Qt.AlignLeft)

        lbl_queue = QtGui.QLabel(self)
        lbl_queue.setText("Players: ")
        lbl_queue.setStyleSheet(
            "QLabel{color: #444; font-weight: bold; font-size: 14px;}"
        )
        box.addWidget(lbl_queue)

        for index, player in enumerate(self.game.player_list):
            lbl = QtGui.QLabel()
            lbl.setText(str(index+1))
            lbl.setFixedHeight(player_height)
            lbl.setFixedWidth(player_width)
            lbl.setAlignment(QtCore.Qt.AlignCenter)
            lbl.setStyleSheet(
                "QLabel{{ background-color : {}; color : {}; border: 3px solid #E64A19; font-weight: bold; border-radius: {};}}"
                    .format(player.background, player.foreground, player_radius)
            )
            self.player_widget_list.append(lbl)
            box.addWidget(lbl)

        return box



    # def generate_player_grid(self):
    #     """ Generates grid to place players """
    #
    #     grd = QtGui.QGridLayout()
    #     grd.setHorizontalSpacing(2)
    #     grd.setVerticalSpacing(2)
    #
    #     for index, player in enumerate(self.game.player_list):
    #         lbl = QtGui.QLabel(self)
    #         lbl.setText(str(index+1))
    #         lbl.setFixedHeight(player_height)
    #         lbl.setFixedWidth(player_width)
    #         lbl.setAlignment(QtCore.Qt.AlignCenter)
    #         lbl.setStyleSheet(
    #             "QLabel{{ background-color : {}; color : {}; border: 3px solid #555; font-weight: bold; border-radius: {};}}"
    #                 .format(player.background, player.foreground, player_radius)
    #         )
    #         grd.addWidget(lbl, 0, index)
    #
    #     return grd

    # def paintEvent(self, event):
    #     qp = QtGui.QPainter()
    #     qp.begin(self)
    #
    #     for tile in self.game.board.tile_set:
    #         qp.fillRect(tile.x * 50, tile.y * 50, 50, 50, QtGui.QColor(tile.background))
    #         qp.setPen(QtGui.QColor(tile.foreground))
    #         qp.drawText(tile.x * 50, tile.y *50, 50, 50, QtCore.Qt.AlignCenter,str(tile.value))
    #     qp.end()


    def init_ui(self):

        # Label Showing Curreint Player Name
        current_player_lbl = QtGui.QLabel(self)
        current_player_lbl.setContentsMargins(0,0,0,10)
        current_player_lbl.setAlignment(QtCore.Qt.AlignCenter)
        current_player_lbl.setObjectName("current_player_lbl")
        current_player_lbl.setText(
            "{}'s Turn".format(self.game.player_list[self.game.cpi].name)
        )
        current_player_lbl.setStyleSheet(
            "QLabel{color: #444; font-weight: bold; font-size: 14px;}"
        )


        # Button to roll the dice by current player
        btn_diceroll = QtGui.QPushButton("Roll The Dice", self)
        btn_diceroll.clicked.connect(self.diceroll)
        btn_diceroll.setCursor(QtCore.Qt.PointingHandCursor)
        btn_diceroll.setStyleSheet(
            "QPushButton{border: 1px solid #ccc; border-radius: 5px; padding: 10px; background: #fff; color: #444; font-weight: bold;} "
            "QPushButton:hover{color: #fff; background: #1565C0;}"

        )

        dice_widget = QtGui.QLabel(self)
        dice_widget.setObjectName("dice")
        dice_widget.setText(dice_face_simulation[0])
        dice_widget.setFixedHeight(80)
        dice_widget.setFixedWidth(80)
        dice_widget.setAlignment(QtCore.Qt.AlignCenter)
        dice_widget.setStyleSheet(
            "QLabel{{ font-size: 30px; background-color : {}; color : {}; border: 2px solid #000; font-weight: bold; border-radius: {};}}"
                .format("#fff5ce", "#000", 5)
        )

        # Game info
        game_info = QtGui.QTextEdit(self)
        game_info.setReadOnly(True)
        game_info.setContentsMargins(0,20,0,0)
        game_info.setStyleSheet(
            "QTextEdit{ font-size: 12px;}"
        )
        game_info.setText(
            "RULES : \n\n"
            "Player can move to board only if s/he rolls 1. \n\n"
            "Player gets additional turn if s/he rolls 1 or 6.\n\n"
            "Red Blocks are for snakes.\n\n"
            "Green box are for Ladders.\n\n"
            "Player eats another player if s/he lands on its current position.\n\n"
            "If a player is eaten, player is moved out of the board.\n\n"
            "If players reaches 100th block s/he wins the game and game resets."
        )

        container_hbox = QtGui.QHBoxLayout()

        vbox2 = QtGui.QVBoxLayout()
        vbox2.setAlignment(QtCore.Qt.AlignTop)

        vbox2_vboxcenter = QtGui.QVBoxLayout()
        vbox2_vboxcenter.setContentsMargins(0, 0, 0, 20)
        vbox2_vboxcenter.setAlignment(QtCore.Qt.AlignCenter)
        vbox2_vboxcenter.addWidget(dice_widget)
        vbox2.addLayout(vbox2_vboxcenter)

        vbox2.addWidget(current_player_lbl)
        vbox2.addWidget(btn_diceroll)
        vbox2.addWidget(game_info)




        # Board Container
        vbox1 = QtGui.QVBoxLayout()
        vbox1.setAlignment(QtCore.Qt.AlignTop)

        vbox1_vbox = QtGui.QVBoxLayout()
        vbox1_vbox.setAlignment(QtCore.Qt.AlignLeft)
        vbox1.addLayout(vbox1_vbox)

        # Grid to represent board

        player_grd = self.generate_player_grid()
        board_grd = self.generate_board_grid()

        vbox1_vbox.addLayout(board_grd)
        vbox1_vbox.addLayout(player_grd)


        container_hbox.addLayout(vbox1)
        container_hbox.addLayout(vbox2)


        self.setLayout(container_hbox)


    def show_winner(self, player):
        msgBox = QtGui.QMessageBox(self)
        msgBox.setWindowTitle("Winner!!!")
        msgBox.setText("Congratuation!!! The winner is : {}".format(player.name))
        msgBox.setStandardButtons(QtGui.QMessageBox.Ok)
        msgBox.exec_()
        self.init_game()


    def update_ply_lbl(self):
        self.findChild(QtGui.QLabel, "current_player_lbl").setText(
            str("{}'s Turn".format(self.game.player_list[self.game.cpi].name))
        )
        """
            https://stackoverflow.com/questions/30639198/pyqt-not-updating-label
            Seems to be a bug which stops the process so following code is executed            
        """
        QtGui.QApplication.processEvents()


    def update_dice_face(self):
        self.findChild(QtGui.QLabel, "dice").setText(dice_face_simulation[self.game.dice.current_face])
        QtGui.QApplication.processEvents()



    def diceroll(self):
        """ Roll the dice and update the state of required widget """

        # Saving initial position of the player_widget
        if not self.player_widget_init_position:
            self.player_widget_init_position = [[widget.geometry().x(), widget.geometry().y()] for widget in self.player_widget_list]

        # Act of rolling a dice
        self.game.roll_dice()

        # Updating the roll
        self.update_dice_face()

        # Updating name for next player
        self.update_ply_lbl()

        for player in self.game.player_list:
            if player.current_tile == len(self.game.board.tile_set):
                self.show_winner(player)



        print self.game.dice.current_face
        print [x.current_tile for x in self.game.player_list]

        for index, pw in enumerate(self.player_widget_list):
            tile_index = self.game.player_list[index].current_tile
            if tile_index != 0:
                widget_index = tile_index - 1
                current_tile_geometry = self.tile_widget_list[widget_index].geometry()
                x = current_tile_geometry.x()
                y = current_tile_geometry.y()
                pw.setGeometry(player_posx_br(x), player_posy_br(y), player_width, player_height)
            else:
                pw.setGeometry(self.player_widget_init_position[index][0], self.player_widget_init_position[index][1], player_width, player_height)


