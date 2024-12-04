from day04 import *
import argparse
from pathlib import Path

def run(args):
    raw_data = get_file_details(args.input)
    grid = raw_data["output"]
    print(grid)

    # Word to search for
    word = "XMAS"

    # Define directions: (dx, dy) corresponds to change in coordinates for each direction
    directions = {
        'N': (0, -1),    
        'S': (0, 1),     
        'E': (1, 0),    
        'W': (-1, 0),   
        'NE': (1, -1),   
        'NW': (-1, -1),  
        'SE': (1, 1),    
        'SW': (-1, 1) 
    }

    # Function to check if the word "XMAS" appears starting from (x, y) in a given direction
    def find_word(grid, x, y, word, direction):
        word_len = len(word)
        dx, dy = directions[direction]
        
        # Try to match the word
        for i in range(word_len):
            new_x = x + i * dx
            new_y = y + i * dy
            
            # Check if the new coordinates are out of bounds
            if new_x < 0 or new_x >= len(grid[0]) or new_y < 0 or new_y >= len(grid):
                return False
            
            # Check if the character matches the word
            if grid[new_y][new_x] != word[i]:
                return False
            
        return True

    # Function to find all occurrences of the word "XMAS" in the grid
    def find_all_occurrences(grid, word):
        occurrences = []
        
        # Loop through every cell in the grid
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                # Check all 8 possible directions
                for direction in directions:
                    if find_word(grid, x, y, word, direction):
                        occurrences.append((x, y))  # Store the coordinates and direction

        return occurrences

    # Find all occurrences of the word "XMAS"
    occurrences = find_all_occurrences(grid, word)

    # Print the results
    for occurrence in occurrences:
        x, y, direction = occurrence
        print(f"Found '{word}' starting at ({x}, {y})")
    
    print(len(occurrences))

def main():
    # Create the argument parser
    parser = argparse.ArgumentParser(description='Process some options.')
    parser.add_argument('--input', type=Path, help='Input file path')
    parser.add_argument('--debug', action='store_true', help='Enable debug mode')

    # Parse the arguments
    args = parser.parse_args()

    run(args)
    
if __name__ == '__main__':
    main()
