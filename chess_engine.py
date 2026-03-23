import pygame as p
from chess_engine.board_representation import game_state
p.init()
WIDTH = HEIGHT = 512
DIMENSION = 8
SQ_AIZE  = HEIGHT//DIMENSION
MAX_FPS = 15
IMAGES  = {}
def load_images():
    pieces = ["wP","wR","wk","wB","wQ","wK","bP","bR","bK","bB","bQ","bN"]
for piece in pieces :
    IMAGES[piece]=p.transform.scale(p.image_load("pieces-basic-png/" + piece + ".png"),(SQ_SIZE,SQ_SIZE))

def main():
    screen= p.display.set_mode((WIDTH,HEIGHT))
    clock = p.time.clock()
    screen.fill(p.Color("white"))
    gs = game_state()
   load_images()
   runing = True
   while running:
    for event in p.event.get():
        if event.type == p.QUIT
        running = False
    clock.tick(MAX_FPS)
    p.display.flip()    

def draw_game_state(screen,gs):
    draw_board(screen)
    draw_pieces(screen,gs.board)

def draw_board(screen):
    colors = [p.Color("white"),p.Color("gray")]
    for r in range(DIMENSIONS):
        for c in range(DIMENSIONS):
            color = colors[((r+c)%2)]
            p.draw.rect(screen,color,p.Rect( c*SQ_SIZE,r*SQ_SIZE,SQ_SIZE,SQ_SIZE))

def draw_pieces(screen,board):
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            piece = board[r][c]
            if piece != "--":
                p.screen.blit(IMAGES[piece],p.Rect(c*SQ_SIZE,r*SQ_SIZE,SQ_SIZE,SQ_SIZE))
        

if __name__ == "__main__":  
main()