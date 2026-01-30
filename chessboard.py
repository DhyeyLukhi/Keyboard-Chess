from pynput.keyboard import Listener, Key
import time
import pyautogui
import json

buffer = ""
pieces = ['K', 'Q', 'R', 'B', 'N']

def go_to_square(move):
    destrank = int(move[-1])
    with open("boardConfig.json", 'r') as file:
        data = json.load(file)

    """X is for the File and Y is for the Rank"""
    y = data['a1']['y']
    x = data['h8']['x']
    width = data['width']
    height = data['height']

    destpixX = x - width*(ord('h') - ord(move[-2]))
    destpixY = y - height*(destrank - 1)

    time.sleep(1)
    print(f"File is {destpixX} and Rank is {destpixY}")

    pyautogui.leftClick(destpixX, destpixY)
    

def pawnmove(pawntomove):
    pass

def on_press(key):
    global buffer

    try:
        buffer += key.char

    except AttributeError:
        if key == Key.backspace:
            buffer = buffer[:-1]

        elif key == Key.enter:
            move = buffer
            if move[0] in pieces:
                """Here will be the code for a piece move"""
            buffer = ""
            go_to_square(move=move)


def main():
    with Listener(on_press=on_press) as listener:
        listener.join()


if __name__ == "__main__":
    main()