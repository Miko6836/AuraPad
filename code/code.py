import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.scanners.keypad import MatrixScanner, KeysScanner
from kmk.modules.combos import Combos, Chord

keyboard = KMKKeyboard()

matrix_scanner = MatrixScanner(
    column_pins=(board.GP4, board.GP5, board.GP6, board.GP7),
    row_pins=(board.GP0, board.GP1, board.GP2, board.GP3),
    columns_to_anodes=DiodeOrientation.COL2ROW,
)


dedicated_pin_scanner = KeysScanner(
    pins=(board.GP9,),
    value_when_pressed=False,
    pull=True,
)


keyboard.matrix = [matrix_scanner, dedicated_pin_scanner]


combos = Combos()
keyboard.modules.append(combos)


keyboard.keymap = [
    [
       
        KC.N7, KC.N8, KC.N9, KC.PSLS,
        KC.N4, KC.N5, KC.N6, KC.PAST,
        KC.N1, KC.N2, KC.N3, KC.PMNS,
        KC.N0, KC.DOT, KC.PENT, KC.PPLS,
        
        
        KC.PSLS, 
    ]
]

combos.combos = [
    Chord((KC.N7, KC.N8), KC.ESC),
    Chord((KC.DOT, KC.PENT), KC.BSPC)
]

if __name__ == '__main__':
    keyboard.go()