import pygame as p
from board_representation import game_state,Move

p.init()

WIDTH = HEIGHT = 512
DIMENSION = 8
SQ_SIZE = HEIGHT // DIMENSION
MAX_FPS = 15
IMAGES = {}

SQ_SELECTED = ()
PLAYER_CLICKED = []

def load_images():
    pieces = ["wP", "wR", "wN", "wB", "wQ", "wK",
              "bP", "bR", "bN", "bB", "bQ", "bK"]
    for piece in pieces:
        IMAGES[piece] = p.transform.scale(
            p.image.load("pieces-basic-png/" + piece + ".png"),
            (SQ_SIZE, SQ_SIZE)
        )

def main():
    global SQ_SELECTED, PLAYER_CLICKED

    screen = p.display.set_mode((WIDTH, HEIGHT))
    clock = p.time.Clock()
    gs = game_state()
    valid_moves = gs.get_valid_moves()
    move_made = False
    load_images()
    running = True

    while running:
        for event in p.event.get():
            if event.type == p.QUIT:
                running = False

            elif event.type == p.MOUSEBUTTONDOWN:
                location = p.mouse.get_pos()
                col = location[0] // SQ_SIZE
                row = location[1] // SQ_SIZE

                if SQ_SELECTED == (row, col):
                    SQ_SELECTED = ()
                    PLAYER_CLICKED = []
                else:
                    SQ_SELECTED = (row, col)
                    PLAYER_CLICKED.append(SQ_SELECTED)

                    if len(PLAYER_CLICKED) == 2:
                        move = Move(
                            PLAYER_CLICKED[0],
                            PLAYER_CLICKED[1],
                            gs.board
                        )
                        if move in valid_moves:
                            gs.make_move(move)
                            move_made = True

                        SQ_SELECTED = ()
                        PLAYER_CLICKED = []
            elif event.type == p.KEYDOWN:
                if event.key == p.K_z:
                    gs.undo_move()
                    move_made = True
        if move_made:
            valid_moves = gs.get_valid_moves()
            move_made = False   
        draw_game_state(screen, gs)
        clock.tick(MAX_FPS)
        p.display.flip()

def draw_game_state(screen, gs):
    draw_board(screen)
    draw_pieces(screen, gs.board)

def draw_board(screen):
    colors = [p.Color("white"), p.Color("gray")]
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            color = colors[(r + c) % 2]
            p.draw.rect(
                screen,
                color,
                p.Rect(c * SQ_SIZE, r * SQ_SIZE, SQ_SIZE, SQ_SIZE)
            )

def draw_pieces(screen, board):
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            piece = board[r][c]
            if piece != "--":
                screen.blit(
                    IMAGES[piece],
                    p.Rect(c * SQ_SIZE, r * SQ_SIZE, SQ_SIZE, SQ_SIZE)
                )

if __name__ == "__main__":
    main()
    