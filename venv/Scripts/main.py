from PIL import Image
import turtle
import chess
from Cboard import Board
from piece import Piece
from player import Player
from rook import Rook
from knight import Knight
from bishop import Bishop
from king import King
from queen import Queen
from pawn import Pawn
import speech_recognition as sr

def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as mic:
        r.energy_threshold = 4000
        audio = r.listen(mic)
        said = ""
        said2 = ""
        print("Diga algo:")
        try:
            said = r.recognize_google(audio, language="es-MX")
            print(said)
        except Exception as e:
            print("Exception " + str(e))
    return said

screen = turtle.Screen()
screen.bgcolor("indigo")
screen.title("Blindfold Chess")
board = chess.Board()

screen.setup (width=800, height=800, startx=400, starty=0)
SQ_SIZE = 4
x = IN_POS_X = -300
y = IN_POS_Y = 270
gif_images = ['bB','bK','bN','bP','bQ','bR','wB','wK','wN','wP','wQ','wR']
white_pawns = []
black_pawns = []

for img in gif_images:
    screen.register_shape("../Pieces/"+ img +".gif")

mychessboard = Board()
screen.tracer(100)
mychessboard.drawBoard()
mychessboard.putWhitePawns(white_pawns)
mychessboard.putBlackPawns(black_pawns)

white_rook_king = Rook(mychessboard.chess_coord["h1"],True)
white_bishop_king = Bishop(mychessboard.chess_coord["f1"],True)
white_knight_king = Knight(mychessboard.chess_coord["g1"],True)
white_rook_queen = Rook(mychessboard.chess_coord["a1"],True)
white_bishop_queen = Bishop(mychessboard.chess_coord["c1"],True)
white_knight_queen = Knight(mychessboard.chess_coord["b1"],True)
white_king = King(mychessboard.chess_coord["e1"],True)
white_queen = Queen(mychessboard.chess_coord["d1"],True)

black_rook_king = Rook(mychessboard.chess_coord["h8"],False)
black_bishop_king = Bishop(mychessboard.chess_coord["f8"],False)
black_knight_king = Knight(mychessboard.chess_coord["g8"],False)
black_rook_queen = Rook(mychessboard.chess_coord["a8"],False)
black_bishop_queen = Bishop(mychessboard.chess_coord["c8"],False)
black_knight_queen = Knight(mychessboard.chess_coord["b8"],False)
black_king = King(mychessboard.chess_coord["e8"],False)
black_queen = Queen(mychessboard.chess_coord["d8"],False)

mychessboard.putwhitePieces(rookq = white_rook_queen ,knightq = white_knight_queen ,bishopq = white_bishop_queen ,queen = white_queen ,king = white_king,bishopk = white_bishop_king ,knightk = white_knight_king ,rookk = white_rook_king )
mychessboard.putblackPieces(rookq = black_rook_queen,knightq = black_knight_queen,bishopq = black_bishop_queen,queen = black_queen,king = black_king,bishopk = black_bishop_king,knightk = black_knight_king,rookk = black_rook_king )

player1 = Player(True)
player2 = Player(False)
running = True
screen.update()
screen.tracer(1)

while(running):
    if player1.has_to_move:
        print("Turno de blancas ")
    else:
        print("Turno de negras ")
    print(board)
    print("Mencione f->casilla_origen")
    try:
        casilla_origen = get_audio()
        casilla_origen = int(casilla_origen.replace("f", ""))
        casilla_origen = chess.square_name(casilla_origen)
        casilla_destino = get_audio()
        casilla_destino = int(casilla_destino.replace("f", ""))
        casilla_destino = chess.square_name(casilla_destino)
        move = chess.Move.from_uci(casilla_origen + casilla_destino)
        move = board.san(move)
        movimiento = board.push_san(move)
        escaque_origen = chess.square_name(movimiento.from_square)  # mover la pieza de la posicion escaque_origen  a escaque_destino
        escaque_destino = chess.square_name(movimiento.to_square)
        mychessboard.show_turtle(escaque_origen)
        mychessboard.delete_turtle(escaque_destino)
        piece_to_move = mychessboard.get_turtle_pos(escaque_origen)
        piece_to_move.setposition(mychessboard.chess_coord[escaque_destino])
    except :
        print("Esa jugada no es posible o no existe")
        move = turtle.textinput("Mejor por el movimiento aqui","Mov : ")
        movimiento = board.push_san(move)
        escaque_origen = chess.square_name(movimiento.from_square)  # mover la pieza de la posicion escaque_origen  a escaque_destino
        escaque_destino = chess.square_name(movimiento.to_square)
        mychessboard.show_turtle(escaque_origen)
        mychessboard.delete_turtle(escaque_destino)
        piece_to_move = mychessboard.get_turtle_pos(escaque_origen)
        piece_to_move.setposition(mychessboard.chess_coord[escaque_destino])

    if board.is_check():
        print("JAQUE MATE")
        board.reset_board()
        running = False
    player1.has_to_move = not(player1.has_to_move)
    player2.has_to_move = not(player1.has_to_move)
    
turtle.mainloop()



