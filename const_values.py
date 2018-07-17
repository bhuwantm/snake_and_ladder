""" Snake positions and ladder position should not have any value similar """

# tile dimension for board
tile_height, tile_width = 50, 50

# Player dimension in board
player_height, player_width = 25 , 25
player_radius = player_width/2

snake_foreground = "#fff"
snake_background = "#f44336"
snake_positions = (
    [17,7],
    [54,34],
    [62,18],
    [64,60],
    [87,24],
    [93,73],
    [95,75],
    [99,78]
)




ladder_positions = (
    [4,14],
    [9,31],
    [20,38],
    [28,84],
    [40,59],
    [50,68],
    [63,81],
    [71,91]
)

ladder_foreground = "#fff"
ladder_background = "#009688"


winner_foreground = "#00897B"
winner_background = "#FDD835"


dice_face_simulation = (
    "dice",
    ".",
    ":",
    ": .",
    ": :",
    ": . :",
    ": : :"
)