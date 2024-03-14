import random

class Crossword:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.grid = [[' ' for _ in range(width)] for _ in range(height)]  # Initialize the grid with empty spaces
        self.words = []  # List to store added words

    def add_word(self, word):
        word = word.upper()  # Convert word to uppercase
        if len(word) > max(self.height, self.width):
            print(f"Word '{word}' is too long to fit in the grid.")
            return
        self.words.append(word)  # Add word to the list
        placed = False
        while not placed:
            direction = random.choice(['across', 'down'])  # Choose a random direction for word placement
            if direction == 'across':  # If the direction is across
                x = random.randint(0, self.width - len(word))
                y = random.randint(0, self.height - 1)
                if self.check_fit(word, x, y, 1, 0):  # Check if the word fits in this position
                    self.place_word(word, x, y, 1, 0)  # Place the word in the grid
                    placed = True
            else:  # If the direction is down
                x = random.randint(0, self.width - 1)
                y = random.randint(0, self.height - len(word))
                if self.check_fit(word, x, y, 0, 1):  # Check if the word fits in this position
                    self.place_word(word, x, y, 0, 1)  # Place the word in the grid
                    placed = True

    def check_fit(self, word, x, y, dx, dy):
        for i in range(len(word)):
            if self.grid[y][x] not in [' ', word[i]]:  # Check if there's already a conflicting character
                return False
            x += dx
            y += dy
        return True

    def place_word(self, word, x, y, dx, dy):
        for i in range(len(word)):
            self.grid[y][x] = word[i]  # Place each character of the word in the grid
            x += dx
            y += dy

    def display(self):
        for row in self.grid:
            print(' '.join(row))  # Display the grid

def main():
    crossword = Crossword(12, 12)  # Create a crossword object with height and width
    words = ["PYTHON", "ALGORITHM", "PROGRAMMING", "COMPUTER", "LANGUAGE"]  # List of words to add
    for word in words:
        crossword.add_word(word)  # Add each word to the crossword
    crossword.display()  # Display the crossword grid

if __name__ == "__main__":
    main()
