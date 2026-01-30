import pynput
import json
import math

print("For the chess board, you have to click on the a1, a8, h1, h8 squares in the correct order")
print("ORDER: a1 -> a8 -> h1 -> h8")
print("Put the cursor at the middle of the square, and once you click, do not click again anywhere on the screen until you complete the task")
print("Now go ahead...")


def configureBlackBoard():
    with open("boardConfig.json", 'r') as file:
        data = json.load(file)

    """X is for the File and Y is for the Rank"""
    y = data['a1']['y']
    x = data['h8']['x']
    width = data['width']
    height = data['height']

    blackPieces = {
        "R1":{
            "x": x - width*(ord('h') - ord('a')), "y" : y
        },
        "N1":{
            "x": x - width*(ord('h') - ord('b')), "y" : y
        },
        "B1":{
            "x": x - width*(ord('h') - ord('c')), "y" : y
        },
        "K":{
            "x": x - width*(ord('h') - ord('e')), "y" : y
        },
        "Q":{
            "x": x - width*(ord('h') - ord('d')), "y" : y
        },
        "B2":{
            "x": x - width*(ord('h') - ord('f')), "y" : y
        },
        "N1":{
            "x": x - width*(ord('h') - ord('g')), "y" : y   
        },
        "R2":{
            "x": x - width*(ord('h') - ord('h')), "y" : y
        }
    }

    with open("blackBoard.json", 'w') as file:
        data = json.dump(blackPieces, file, indent=4)


def configureWhiteBoard():
    with open("boardConfig.json", 'r') as file:
        data = json.load(file)

    """X is for the File and Y is for the Rank"""
    y = data['a1']['y']
    x = data['h8']['x']
    width = data['width']
    height = data['height']

    whitePieces = {
        "R1":{
            "x": x - width*(ord('h') - ord('a')), "y" : y
        },
        "N1":{
            "x": x - width*(ord('h') - ord('b')), "y" : y
        },
        "B1":{
            "x": x - width*(ord('h') - ord('c')), "y" : y
        },
        "Q":{
            "x": x - width*(ord('h') - ord('d')), "y" : y
        },
        "K":{
            "x": x - width*(ord('h') - ord('e')), "y" : y
        },
        "B2":{
            "x": x - width*(ord('h') - ord('f')), "y" : y
        },
        "N1":{
            "x": x - width*(ord('h') - ord('g')), "y" : y   
        },
        "R2":{
            "x": x - width*(ord('h') - ord('h')), "y" : y
        }
    }

    with open("whiteBoard.json", 'w') as file:
        data = json.dump(whitePieces, file, indent=4)


class MouseCapture:
    def __init__(self):
        self.positions = ['a1X', 'a1Y', 'a8X', 'a8Y', 'h1X', 'h1Y', 'h8X', 'h8Y']
        self.index = 0  
        self.listener = None

    def on_click(self, posX, posY, button, pressed):
        if pressed and button == pynput.mouse.Button.left:
            if self.index < len(self.positions):
                self.positions[self.index] = posX
                self.index += 1
                self.positions[self.index] = posY
                self.index += 1
                print(f"Click {self.index // 2} captured: X={posX}, Y={posY}")
                
                if self.index >= len(self.positions):
                    print("All positions captured!")
                    self.listener.stop()

    def start(self):
        self.listener = pynput.mouse.Listener(on_click=self.on_click)
        with self.listener:
            self.listener.join()


def main():
    capture = MouseCapture()
    capture.start()

    boardConfig = {
        "a1": {"x": capture.positions[0], "y": capture.positions[1]},
        "a8": {"x": capture.positions[2], "y": capture.positions[3]},
        "h1": {"x": capture.positions[4], "y": capture.positions[5]},
        "h8": {"x": capture.positions[6], "y": capture.positions[7]},

        "width": (capture.positions[4] - capture.positions[0])/7,
        "height": ((capture.positions[1] - capture.positions[3])/7)

    }

    with open("boardConfig.json", 'w') as file:
        data = json.dump(boardConfig, file, indent=4)

if __name__ == "__main__":
    main()