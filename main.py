from itertools import izip

import sys
from PyQt4 import QtGui
from window import GameWindow


def main():
    """ Initializes the window """
    app = QtGui.QApplication(sys.argv)
    GUI = GameWindow()
    sys.exit(app.exec_())

main()


""" Future Improvements """
# TODO: Smooth animation for updating plyaer position
# TODO: Add dialogue for Dynamic initalization of players
# TODO: Update to responsive UI
# TODO: Add Grphics for snake and ladder position
# TODO: Add Tests